from .models import Planning, Ligne, Conditions
from users.models import Clients
from rest_framework import serializers


class LigneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ligne
        fields = '__all__'
        
class LignesSerializerForPlanning(serializers.ModelSerializer):
    
    class Meta:
        model = Ligne
        fields = ["id","agent_type","start_date","end_date","week_days","month_days","selected_days","pause","agent_number","start_hour","end_hour","isPausePaid","start_cutoff","end_cutoff"]
    
class ConditionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Conditions
        fields = '__all__'



class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planning
        fields = '__all__'

class PlanningSerializerForClient(serializers.ModelSerializer):
    lignes = LigneSerializer(many=True)
    conditions = ConditionsSerializer()
    class Meta:
        model = Planning
        fields = ["id","total_hours","site_name","state","lignes","start_planning_date","conditions"]
        
        
        
class PlanningSerializerForAgent(serializers.ModelSerializer):
 
    class Meta:
        model = Planning
        fields = '__all__'
 