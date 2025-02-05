from django.shortcuts import render
from rest_framework import generics
from .models import Planning, Ligne
from .serializers import PlanningSerializer,LigneSerializer,LignesSerializerForPlanning
from django.db import DatabaseError, transaction,IntegrityError
from rest_framework.response import Response
from rest_framework import status
from users.pagination import CustomPageNumberPagination
from django.shortcuts import get_object_or_404
from .models import Planning, Ligne
from rest_framework import filters
import django_filters
from .filters import PlanningListFilter


from .utils import calculate_all_hours
# Create your views he
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
                if Planning_serializer.is_valid():
                    sid = transaction.savepoint()
                    Planning= Planning_serializer.save()
                    hours =0
                    for ligne in request.data['lignes']:
                        print(Planning_serializer.validated_data)
                        ligne['planning'] = Planning.id
                        ligne_serializer = LigneSerializer(data=ligne)
                        print(ligne)
                        if ligne_serializer.is_valid():
                            ligne_serializer.save()
                            hours += calculate_all_hours(ligne)*(ligne["month_days"].count("y"))

                            
                        
                        else:
                            transaction.savepoint_rollback(sid) 
                            return Response(ligne_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                    print(hours)
                    Planning_serializer.validated_data['total_hours'] = hours  # Update the field
                    Planning_serializer.save(total_hours=hours)  # Pass the field while saving
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
    serializer_class = PlanningSerializer
    def get(self,request,*args,**kwargs):
        planning = get_object_or_404(Planning, pk=kwargs.get("pk"))  # Returns 404 if not found
        lignes = Ligne.objects.filter(planning=planning)
    
        planning_serializer = PlanningSerializer(planning)
        lignes_serializer = LignesSerializerForPlanning(lignes, many=True)

        data = {
        "planning": {
            **planning_serializer.data,
            "lignes": lignes_serializer.data
        }
    }

        return Response(data)