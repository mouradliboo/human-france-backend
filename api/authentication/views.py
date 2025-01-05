from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CustomObtainTokenSerializer
from .docstring import login_schema
class CustomTokenObtain(TokenObtainPairView):
    serializer_class = CustomObtainTokenSerializer
    
    @login_schema()  
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
