
from django.shortcuts import render
from .models import Tarefa
from datetime import date

def lista_tarefas(request):
    
    tarefas = Tarefa.objects.all()
    
    hoje = date.today()

    context = {
        'tarefas': tarefas,
        'hoje': hoje,
    }
    
    return render(request, 'listatarefas/lista.html', context)