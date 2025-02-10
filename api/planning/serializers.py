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
        
class LignesSerializerForPlanning(serializers.ModelSerializer):
    
    class Meta:
        model = Ligne
        fields = ["id","agent_type","start_date","end_date","week_days","month_days","selected_days","pause","agent_number","start_hour","end_hour","isPausePaid","start_cutoff","end_cutoff"]