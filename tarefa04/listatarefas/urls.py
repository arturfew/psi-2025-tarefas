# Conteúdo completo do novo arquivo listatarefas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
]