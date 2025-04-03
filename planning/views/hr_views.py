from django.db import connection
from django.shortcuts import render
from rest_framework import generics
from ..models import Planning, Ligne, Conditions,PlanningAgent,Absences
from ..serializers.serializers import (PlanningSerializer,LigneSerializer,
                                       PositionnementSerializer,
                                       PositionnementPostSerializer,
                                       PlanningSerializerForClient,
                                       
                                       PlanningDetailsSerializer,
                                       ConditionsSerializer)

from django.db import (DatabaseError,
                       transaction,
                       IntegrityError)
from rest_framework.response import Response
from rest_framework import status,mixins
from users.pagination import CustomPageNumberPagination
from django.shortcuts import get_object_or_404
from ..models import Planning, Ligne
from rest_framework import filters
import django_filters
import datetime
from users.models import Clients
import json
from django.utils import  timezone
from rest_framework.decorators import api_view
from ..serializers.hr_serializers import (AbsencesCreateSerializer,
                                          AbsencesSerializer,)
from rest_framework.exceptions import ValidationError
from planning.exceptions import AgentNotWorkingException
from django.db import IntegrityError, transaction
from rest_framework import status, generics, permissions
from datetime import datetime
import pytz

class AbsencesList(generics.ListCreateAPIView):
    queryset = Absences.objects.all()
    serializer_class = AbsencesSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        planning_agent= request.data.get('planning_agent')
        a = request.data.get('absence_date')
        absence_date = datetime.strptime(a, "%Y-%m-%d").replace(tzinfo=pytz.UTC)
        day = absence_date.day
    
        absence_serializer = AbsencesCreateSerializer(data=request.data)
        if absence_serializer.is_valid():
            try:
                with transaction.atomic():
                    absence_serializer.save()
                    # Update the planning agent's position  to 'absent'
                    planning_agent_instance = get_object_or_404(PlanningAgent, id=planning_agent)
                    if planning_agent_instance.position[int(day)-1]['works'] != True:
                            raise AgentNotWorkingException("Agent is not working on this day.")
                    planning_agent_instance.position[int(day)-1]["status"] = 'absent'
                    print(planning_agent_instance.position[int(day)-1])
                    # taking the vacation up in the planning matrix 
                    if absence_date.date() < timezone.now().date():
                        planning_agent_instance.save()
                        return Response(absence_serializer.data, status=status.HTTP_201_CREATED)
                    # Update the days_needs field in the Ligne model
                    # Get the Ligne instance associated with the PlanningAgent in that day 

                        
                    ligne_id = (
                                   planning_agent_instance.position[int(day)-1].get('id') 
                                  or planning_agent_instance.position[int(day)-1].get('id2')
                                )
                    ligne = get_object_or_404(Ligne, id=ligne_id)
                    days_needs = ligne.days_needs.split(",")
                    days_needs[int(day)-1]= str(int(days_needs[day-1])+ 1)
                    ligne.days_needs = ",".join( days_needs)      
                    ligne.save()              
                    planning_agent_instance.save()
                    return Response(absence_serializer.data, status=status.HTTP_201_CREATED)
        
            
            except IntegrityError:
                return Response({"error": "Integrity error occurred."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            return Response(absence_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AbsencesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Absences.objects.all()
    serializer_class = AbsencesSerializer
    @transaction.atomic
    def delete(self,request,*args,**kargs):
     try:
       with transaction.atomic():
        absence = Absences.objects.filter(id=kargs['pk']).select_related('planning_agent').first()
        print( absence.absence_date)
        day = absence.absence_date.day
        planning_agent = absence.planning_agent
        # Update the planning agent's position  to 'work'
        planning_agent.position[int(day)-1]["status"] = 'work'
        # Update the days_needs field in the Ligne model
        if absence.absence_date > timezone.now().date():
            ligne_id = (
                           planning_agent.position[int(day)-1].get('id') 
                          or planning_agent.position[int(day)-1].get('id2')
                        )
            ligne = get_object_or_404(Ligne, id=ligne_id)
            days_needs = ligne.days_needs.split(",")
            days_needs[int(day)-1]= str(int(days_needs[day-1])- 1)
            ligne.days_needs = ",".join( days_needs)      
            ligne.save()
        planning_agent.save()
        absence.delete()
        return Response({"message": "Absence deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
     except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        

   