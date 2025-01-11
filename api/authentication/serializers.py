from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from rest_framework import serializers
from authentication.utils.createAgent import generate_random_string



class CustomObtainTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token["role"]= user.role
        token["id"]=user.id
        return token
    def validate(self, attrs):
        data = super().validate(attrs)

        data['email'] = self.user.email
        data['role'] = self.user.role
        data['id'] = self.user.id
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","first_name","last_name","email","phone","address"]
       

    def create(self, validated_data):
        username = f"{validated_data.get('email')}{validated_data.get('first_name')}"
        user = CustomUser.objects.create_user(username=username,
                                             
                                              **validated_data)
        return user
