from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CustomObtainTokenSerializer
from rest_framework.decorators import permission_classes
from django.http import JsonResponse
from .docstring import login_schema
import cloudinary.uploader
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import UserSerializer
from users.serializers import AgentSerializerCreate
class CustomTokenObtain(TokenObtainPairView):
    serializer_class = CustomObtainTokenSerializer
    
    @login_schema()  
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@permission_classes([AllowAny])
@api_view(['POST'])
def signup(request):
    try:
        # Validate user data
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            # Save the user and retrieve the instance
            user = user_serializer.save()

            # Add user_id to the request data for Agent creation
            agent_data = request.data.copy()
            agent_data['user'] = user.id

            # Validate and save agent data
            agent_serializer = AgentSerializerCreate(data=agent_data)
            if agent_serializer.is_valid():
                agent_serializer.save()
                return JsonResponse({"agent":agent_serializer.data,
                                     "user":user_serializer.data}, status=201)
            else:
                # Delete the created user if agent creation fails
                user.delete()
                print("hhhhh user deleted")
                return JsonResponse(agent_serializer.errors, status=400)
        else:
            return JsonResponse(user_serializer.errors, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
