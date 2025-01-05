from django.urls import path,include
from .views import listInscription,listDesAgents
urlpatterns = [
    path('agents_inscription_list/', listInscription),
    path('agents_list/', listDesAgents),
]
# Create