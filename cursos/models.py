from django.db import models

# Create your models here.

class Cursos(models.Model):
    nome = models.CharField(max_length=40)
    carga_horaria = models.IntegerField()
    data_criacao = models.DateTimeField()
    ativo = models.BooleanField(default=True)