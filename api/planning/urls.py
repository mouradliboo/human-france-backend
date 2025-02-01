from django.urls import path,include
from .views import PlanningList, PlanningDetail
urlpatterns = [
  path('', PlanningList.as_view(), name='planning-list'),
   path('<int:pk>/', PlanningDetail.as_view(), name='planning-detail'),
   ]