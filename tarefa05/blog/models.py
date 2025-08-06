from django.db import models
from datetime import date
# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField( max_length=50)
    descricao = models.TextField()
    data = models.DateField(date.today)
    imagem = models.ImageField( upload_to="media/",null=True, blank=True)
    def __str__(self):
        return self.titulo
class Header(models.Model):
    titulo = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo
class Footer(models.Model):
    descricao = models.TextField()
    
