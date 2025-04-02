from django.urls import path,include
from .views.views import(
   PlanningList, 
   PlanningDetail, 
   PlanningListAgent,
   PositionnementList,
   PositionnmentAgentFilterList,
   
    supprimerVacation,
    test,
    PositionnementDetail,
    LigneList, conditionsOfPlanning,
    LigneDetail,
    ConditionsList, ConditionsDetail)
from .views.hr_views import (AbsencesList,)

urlpatterns = [
  path('planning/', PlanningList.as_view(), name='planning-list'),
   path('planning/<int:pk>/', PlanningDetail.as_view(), name='planning-detail'),
   path('planning/<int:pk>/conditions/',conditionsOfPlanning ),
   path('lignes/', LigneList.as_view(), name='ligne-list'),
   path('lignes/supprimerVacation',supprimerVacation),
    path('lignes/<int:pk>/', LigneDetail.as_view(), name='ligne-detail'),
    path('conditions/',ConditionsList.as_view(),name='Conditions-list'),
    path('conditions/<int:pk>/',ConditionsDetail.as_view(),name='Conditions-detail'),
    path('planning/agents/',PlanningListAgent.as_view(),name='planning-list-agent') ,
    path('planning/position/',PositionnementList.as_view(),name='planning-list-agent'),
    path('planning/position/<int:pk>/',PositionnementDetail.as_view(),name='planning-list-agent'),
    path('planning/positionAgent/',PositionnmentAgentFilterList.as_view(),name='planning-list-agent'),
    path('planning/absences/',AbsencesList.as_view(),name='absences-list'),
    
    
    path('test/',test),
   
   ]