from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from rest_framework import serializers

from django.core.mail import send_mail
def sendMail(username,email):
            send_mail(
    "Welcome to our platform",
     f"Hello {username},\n\nWelcome to our platform. We are happy to have you as a new user.\n\nBest regards,\n\nThe team",
     from_email= "ma_missoum@esi.dz",
     recipient_list=[email],
    fail_silently=False,
)


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
        fields = ["id","username","first_name","last_name","email","phone","address","password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
