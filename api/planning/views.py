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


from .utils import calculate_all_hours,calculate_volume_horaire
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
        planning.total_hours = volume_horaire
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
        planning_id = instance.planning# Store ID before deleting
        instance.delete()          # ✅ Default behavior (delete)
        planning = Planning.objects.get(id=planning_id)
        volume_horaire = calculate_volume_horaire(planning)
        planning.total_hours = volume_horaire
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
                            hours += calculate_all_hours(ligne)                            
                        
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
    def patch(self,request,*args,**kwargs):
        planning = get_object_or_404(Planning, pk=kwargs.get("pk"))
        if request.data.get("lignes"):
            lignes = request.data.pop("lignes")
            