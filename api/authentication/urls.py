from rest_framework_simplejwt.views import  TokenRefreshView
from django.urls import path,include
from .views import CustomTokenObtain
urlpatterns = [
        path('login/', CustomTokenObtain.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]