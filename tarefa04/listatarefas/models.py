
from django.db import models

class Tarefa(models.Model):
  
    nome = models.CharField(max_length=200)
    prazo = models.DateField()
    
   
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Concluída', 'Concluída'),
        ('Cancelada', 'Cancelada'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')

   
    def __str__(self):
        return self.nome
