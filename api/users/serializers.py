from .models import CustomUser
from rest_framework import serializers
from .models import AgentProfile



class UserSerializerForInscription(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","first_name","last_name","email","phone","address"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user   

class AgentSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = AgentProfile
        fields = '__all__'  
class AgentDetailSerializer(serializers.ModelSerializer):
    user = UserSerializerForInscription()
    class Meta:
        model = AgentProfile
        fields = '__all__'  
class AgentListInscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializerForInscription()
    class Meta:
        model = AgentProfile
        fields = ['id','user','updated_at']
