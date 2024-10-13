"""
URL configuration for nexisconnect_connect project.

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
from django.urls import path, include
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Nexis Connect API",
      default_version='v1',
      description="API for Nexis Connect",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shkwahab60@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
    public=False,  # Change this to False to restrict access
    permission_classes=(permissions.IsAdminUser,),  # Require authentication
)
urlpatterns = [
    # Swagger UI documentation
    path('api/documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc documentation
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Schema for JSON
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(), name='schema-json'),
    path('admin/', admin.site.urls),
    path("api/", include("adminside.urls")),
]
