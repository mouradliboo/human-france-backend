from django.urls import path,include
from .views import PlanningList, PlanningDetail, LigneList, LigneDetail
urlpatterns = [
  path('', PlanningList.as_view(), name='planning-list'),
   path('<int:pk>/', PlanningDetail.as_view(), name='planning-detail'),
   path('lignes/', LigneList.as_view(), name='ligne-list'),
    path('lignes/<int:pk>/', LigneDetail.as_view(), name='ligne-detail'),
   
   ]