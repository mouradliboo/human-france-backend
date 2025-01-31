from django.shortcuts import render
from rest_framework import generics
from .models import Planning, Ligne
from .serializers import PlanningSerializer,LigneSerializer
# Create your views he
class PlanningList(generics.ListCreateAPIView):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer
   
        
        
        
        
class PlanningDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer
    
    
    
    