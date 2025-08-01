# Conteúdo completo de listatarefas/models.py
from django.db import models

class Tarefa(models.Model):
    # Definindo os campos (colunas da tabela)
    nome = models.CharField(max_length=200)
    prazo = models.DateField()
    
    # Opções para o campo 'status'
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')

    # Esta função define como o objeto será exibido no Admin
    def __str__(self):
        return self.nome
