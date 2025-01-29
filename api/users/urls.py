from django.urls import path,include
from .views import agentDetail,AgentList
urlpatterns = [
    path('agents/', AgentList.as_view()),
   path('agents/<int:pk>/', agentDetail),   
   ]
# Create