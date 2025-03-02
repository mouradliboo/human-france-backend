"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from authentication.models import CustomUser
import pdfkit
from rest_framework.response import Response
from xhtml2pdf import pisa
from rest_framework.decorators import api_view
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="API documentation for My Django project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)
@api_view(['GET'])
def test(request):
   
  print("hhhhhhhhhhhhhhh")

  html_content = "<h1 style='color: red;'>Hello, PDF!</h1>"
  with open("pdfs/out.pdf", "wb") as pdf_file:
     pisa.CreatePDF(html_content, dest=pdf_file)

  return Response({"message":"pdf generated"})

urlpatterns = [
    path('admin/', admin.site.urls),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  
  path('',test),
                     
    path('api/v1/auth/' , include('authentication.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/', include('planning.urls')),
]
