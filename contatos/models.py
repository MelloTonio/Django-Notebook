from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=255,blank=True) 

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200,blank=True)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200,blank=True)
    data_criaçao = models.CharField(max_length=30,default=timezone.now,blank=True)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    def __str__(self):
        return self.nome
