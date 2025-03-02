from django.urls import path,include
from .views import agentDetail,AgentList,ClientsList
urlpatterns = [
    path('agents/', AgentList.as_view()),
   path('agents/<int:pk>/', agentDetail),  
   path('clients/',ClientsList.as_view()) ,
   ]
# Create