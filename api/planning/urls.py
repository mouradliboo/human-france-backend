from django.urls import path,include
from .views import PlanningList, PlanningDetail, LigneList, conditionsOfPlanning,LigneDetail, ConditionsList, ConditionsDetail
urlpatterns = [
  path('planning/', PlanningList.as_view(), name='planning-list'),
   path('planning/<int:pk>/', PlanningDetail.as_view(), name='planning-detail'),
   path('planning/<int:pk>/conditions/',conditionsOfPlanning ),
   path('lignes/', LigneList.as_view(), name='ligne-list'),
    path('lignes/<int:pk>/', LigneDetail.as_view(), name='ligne-detail'),
    path('conditions/',ConditionsList.as_view(),name='Conditions-list'),
    path('conditions/<int:pk>/',ConditionsDetail.as_view(),name='Conditions-detail'),
    
   
   ]