# Conteúdo completo de listatarefas/views.py
from django.shortcuts import render
from .models import Tarefa
from datetime import date # Importa a biblioteca de data

def lista_tarefas(request):
    # Busca todos os objetos Tarefa no banco de dados
    tarefas = Tarefa.objects.all()
    
    # Pega a data de hoje
    hoje = date.today()
    
    # Envia os dados para o template
    context = {
        'tarefas': tarefas,
        'hoje': hoje,
    }
    
    return render(request, 'listatarefas/lista.html', context)