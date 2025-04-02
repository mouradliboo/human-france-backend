from ..models import Planning, Ligne, Conditions,PlanningAgent,Absences
from users.models import Clients
from rest_framework import serializers
from users.serializers import AgentListInscriptionSerializer


class PlanningSerializerForAbcenses(serializers.ModelSerializer):
    class Meta:
        model = Planning
        fields = ['id','site_name','start_planning_date',]

class PositionnementForAbsencesSerializer(serializers.ModelSerializer):
    agent  = AgentListInscriptionSerializer()
    planning =PlanningSerializerForAbcenses()
    class Meta:
        model = PlanningAgent
        fields = ['id','agent','planning']
class AbsencesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absences
        fields = '__all__'
class AbsencesSerializer(serializers.ModelSerializer):
    planning_agent=PositionnementForAbsencesSerializer()
    class Meta:
        model = Absences
        fields = '__all__'
