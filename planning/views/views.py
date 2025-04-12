from django.db import connection
from django.shortcuts import render
from rest_framework import generics
from ..models import Planning, Ligne, Conditions,PlanningAgent
from ..serializers.serializers import (PlanningSerializer,LigneSerializer,
                                       PositionnementSerializer,
                                       PositionnementPostSerializer,
                                       PlanningSerializerForClient,
                                       PlanningDetailsSerializer,
                                       ConditionsSerializer,
                                       PositionnementFilterSerializer,
                                       )

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
from ..filters import PlanningListFilter,PositionnementFilter
from users.models import Clients
import json
from rest_framework.decorators import api_view
from django.db import IntegrityError, transaction



from ..utils import calculate_all_hours,calculate_volume_horaire
# Create your views he



class LigneList(generics.ListCreateAPIView):
    queryset = Ligne.objects.all()
    serializer_class = LigneSerializer
    def post(self, request, *args, **kwargs):
      try: 
        data = request.data

        # Identify by a unique field (e.g., `id` or combination of fields)
        ligne_id = data.get("id")  # Assuming `id` is provided in the request

        if ligne_id:
            # Try to update existing record
            ligne, created = Ligne.objects.update_or_create(
                id=ligne_id,
                defaults=data  # Use `defaults` to update other fields
            )
        else:
            # If no ID, create a new record
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            ligne = serializer.save()
            created = True

        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        planning = Planning.objects.get(id=data.planning)
        volume_horaire = calculate_volume_horaire(planning)
        planning.total_hours = volume_horaire["volume_horaire"]
        planning.start_planning_date = volume_horaire["start_date"]
        planning.save()
        return Response(LigneSerializer(ligne).data, status=status_code)
      except IntegrityError as e:
            print(e)
            return Response({"error":"IntegrityError"},status=status.HTTP_400_BAD_REQUEST)
      except DatabaseError as e:
            print(e)
            return Response({"error":"DatabaseError"},status=status.HTTP_400_BAD_REQUEST)
      except Exception as e:
            print(e)
            return Response({"error":"DatabaseError"},status=status.HTTP_400_BAD_REQUEST)
class LigneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ligne.objects.all()
    serializer_class = LigneSerializer
    def perform_destroy(self, instance):
        """Handles DELETE request, calls function after deletion."""
        instance_id = instance.id 
        planning = instance.planning# Store ID before deleting
        instance.delete()          # ✅ Default behavior (delete)
        volume_horaire = calculate_volume_horaire(planning)
        planning.total_hours = volume_horaire["volume_horaire"]
        planning.start_planning_date = volume_horaire["start_date"]
        planning.save()
class PlanningList(generics.ListCreateAPIView):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer
    pagination_class= CustomPageNumberPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter)
    filterset_class = PlanningListFilter
    search_fields = ['$site_name']
    def post(self,request,*args,**kwargs):
      try:
         with transaction.atomic():
             
              
            
                Planning_serializer = PlanningSerializer(data=request.data)
                sid = transaction.savepoint()

                if Planning_serializer.is_valid():
                    Planning= Planning_serializer.save()
                    hours =0
                    min_date = None
                    for ligne in request.data['lignes']:
                        ligne['planning'] = Planning.id
                        ligne_serializer = LigneSerializer(data=ligne)
                        if ligne_serializer.is_valid():
                            ligne_serializer.save()
                            if min_date is None or min_date > ligne['start_date']:
                                min_date = ligne['start_date']
                            
                            hours += calculate_all_hours(ligne)                            
                        
                        else:
                            transaction.savepoint_rollback(sid) 
                            return Response(ligne_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                    Planning_serializer.validated_data['total_hours'] = hours  # Update the field
                    Planning_serializer.validated_data['start_planning_date'] = min_date  # Update the field
                    Planning_serializer.save(total_hours=hours,
                                             start_planning_date=min_date)  # Pass the field while saving
                    transaction.savepoint_commit(sid)
                    return Response(Planning_serializer.data,status=status.HTTP_201_CREATED)
                else : 
                    transaction.savepoint_rollback(sid)
                    return Response(Planning_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      except IntegrityError as e:
            transaction.savepoint_rollback(sid)
            print(e)
            return Response({"error":"IntegrityError"},status=status.HTTP_400_BAD_REQUEST)
            
       

       
   
        
        
        
        
class PlanningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planning.objects.all()
    serializer_class = PlanningDetailsSerializer
  
    def patch(self, request, *args, **kwargs):
     try:
        planning = get_object_or_404(Planning, pk=kwargs.get("pk"))
        sid = transaction.savepoint()

        shouldUpdateTime = False
        if request.data.get("lignes"):
            shouldUpdateTime = True
            lignes = request.data.get("lignes",[])
            for ligne in lignes:
                ligne_id = ligne.get("id",None)
                if ligne_id:   #if updating existing ligne
                   
                        ligne_to_update = get_object_or_404(Ligne, pk=ligne_id)  
                        ligne_serializer = LigneSerializer(ligne_to_update, data=ligne, partial=True)
                        if ligne_serializer.is_valid():
                            ligne_serializer.save()
                        else:
                            return Response(ligne_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
              
                else:# creating new ligne
                    ligne_serializer = LigneSerializer(data=ligne) 
                    if ligne_serializer.is_valid():
                        ligne_serializer.save()
                    else:
                        return Response(ligne_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.data.get("site_name"):  # ✅ Fixed request.data["site_name"] to .get()
            planning.site_name = request.data["site_name"]
        if request.data.get("client"):
            planning.client = Clients.objects.get(pk=request.data["client"])
        if request.data.get("state"):
            planning.state = request.data["state"]

        if shouldUpdateTime:
            volume_horaire = calculate_volume_horaire(planning)
            planning.total_hours = volume_horaire["volume_horaire"]
            planning.start_planning_date = volume_horaire["start_date"]

        planning.save()
        transaction.savepoint_commit(sid)
        return Response(PlanningSerializer(planning).data)

     except IntegrityError as e:
        print(e)
        transaction.savepoint_rollback(sid)
        return Response({"error": "IntegrityError"}, status=status.HTTP_400_BAD_REQUEST)
     except DatabaseError as e:
        print(e)
        transaction.savepoint_rollback(sid)
        return Response({"error": "DatabaseError"}, status=status.HTTP_400_BAD_REQUEST)
     except Exception as e:
        print(e)
        transaction.savepoint_rollback(sid)
        return Response({"error": "Error"}, status=status.HTTP_400_BAD_REQUEST)



class ConditionsList(generics.ListCreateAPIView):
    queryset = Conditions.objects.all()
    serializer_class = ConditionsSerializer
    
    def post(self,request, *args, **kwargs):
     try:

        # Make a mutable copy of request.data

        # Convert "experience" field to JSON string if it exists


        # Serialize data
         conditions_serializer = ConditionsSerializer(data=request.data)

         if conditions_serializer.is_valid():
            conditions = conditions_serializer.save()

            # Retrieve planning object using the correct key
            planning_id = request.data.get("planning", None)
            if planning_id is None:
                return Response({"error": "Planning ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            planning = get_object_or_404(Planning, pk=planning_id)

            # Link the new conditions to the planning instance
            planning.conditions = conditions
            planning.save()

            return Response(conditions_serializer.data, status=status.HTTP_201_CREATED)
         else:
            return Response(conditions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     except IntegrityError as e:
        print(e)
        return Response({"error": "IntegrityError"}, status=status.HTTP_400_BAD_REQUEST)
     except DatabaseError as e:
        print(e)
        return Response({"error": "DatabaseError"}, status=status.HTTP_400_BAD_REQUEST)
     except Exception as e:
        print(e)
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, Update, and Delete View for a Single Condition
class ConditionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conditions.objects.all()
    serializer_class = ConditionsSerializer
    
@api_view(['GET'])
def conditionsOfPlanning(request, pk):
    try:
        planning = Planning.objects.get(id=pk)
        conditions = planning.conditions
        conditions_serializer = ConditionsSerializer(conditions)
        return Response(conditions_serializer.data)
    except Planning.DoesNotExist:
        return Response({"error": "Planning not found"}, status=status.HTTP_404_NOT_FOUND)
    except Conditions.DoesNotExist:
        return Response({"error": "Conditions not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    


    

class PlanningListAgent(generics.ListAPIView):
    queryset =  Planning.objects.prefetch_related("lignes").all()
    serializer_class = PlanningSerializerForClient
    pagination_class= CustomPageNumberPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter)
    filterset_class = PlanningListFilter
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class PositionnementList(generics.ListCreateAPIView):
    queryset = PlanningAgent.objects.all()
    pagination_class= CustomPageNumberPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter)
    filterset_class = PositionnementFilter
    def get_serializer_class(self):
     if self.request.method == 'POST':
        return PositionnementPostSerializer
     return PositionnementSerializer

    
    
class PositionnementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlanningAgent.objects.all()
    serializer_class = PositionnementSerializer
   
class PositionnmentAgentFilterList(generics.ListAPIView):
    queryset = PlanningAgent.objects.filter(status="accepted").all()
    serializer_class = PositionnementFilterSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter)
    filterset_class = PositionnementFilter


@transaction.atomic 
@api_view(['POST'])   
def supprimerVacation(request):
    position = request.data.get('position_id') 
    ligne_id = request.data.get("ligne_id")
    day = request.data.get("day")
    try:
        ligne = get_object_or_404(Ligne, id=ligne_id)
        days_needs = ligne.days_needs.split(",")
        days_needs[int(day)-1]= str(int(days_needs[day-1])- 1)
        ligne.days_needs = ",".join( days_needs)
        agent_position = get_object_or_404(PlanningAgent, id=position)
        agent_position.position[int(day)-1]["status"] = "free"
        agent_position.position[int(day)-1]["startHour"] = None
        agent_position.position[int(day)-1]["endHour"] = None
        agent_position.position[int(day)-1]["id"] = None
        agent_position.position[int(day)-1]["id2"] = None
        ligne.save()
        agent_position.save()
        
        
        return Response({"message":"done successfully"},status=status.HTTP_200_OK)
    except Ligne.DoesNotExist:
        return Response({"error": "Ligne not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    

    
    
    
  
            
    
   