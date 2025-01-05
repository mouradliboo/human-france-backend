from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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
