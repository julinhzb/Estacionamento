from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o painel de administração do Django
    path('', include('estacionamento.urls')),
    path('agendar/', views.agendar, name='agendar'),
    path('sucesso/', views.sucesso, name='sucesso'),
]
