from django.contrib import admin
from django.urls import path, include  # <--- Importante: agregar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esto conecta las URLs de tu app con el proyecto principal
    path('', include('app_Guarderia.urls')), 
]