from .models import Planning, Ligne
from users.models import Clients
from rest_framework import serializers
class PlanningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planning
        fields = '__all__'
class LigneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ligne
        fields = '__all__'