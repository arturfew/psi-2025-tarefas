# Conteúdo completo de listatarefas/admin.py
from django.contrib import admin
from .models import Tarefa

# Registra o modelo Tarefa para que ele apareça no site do admin
admin.site.register(Tarefa)
