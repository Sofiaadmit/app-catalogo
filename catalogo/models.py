from django.db import models

class Obra(models.Model):
    TIPO_CHOICES = [
        ("Filme", "Filme"),
        ("Série", "Série"),
    ]

    tiulo = models.CharField(max_length=150) # quantidade de caracteres
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100)
    descricao = models.TextField() #permite criar um bloco de texto 

    def __str__(self):
        return self.titulo 


