from django.urls import path,include
from .views import list_agents,agentDetail
urlpatterns = [
    path('agents/', list_agents),
   path('agents/<int:pk>/', agentDetail),   
   ]
# Create