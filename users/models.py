from django.db import models
from django.contrib.auth.models import User
#from hackaton.models import Hackaton
# sury <3

class Lenguaje(models.Model):
    nombreLenguaje = models.CharField(max_length=255)
    indefinido = 'indefinido'

    objetivoTupla = (
        (indefinido, 'indefinido'),
        ('objetos', 'orientado a objetos'),
        ('eventos', 'orientado a eventos'),
        ('hibrido', 'hibrido'),
    )
    objetivo = models.CharField(max_length=255, choices=objetivoTupla, default=indefinido)

    def __str__(self):
	       return self.nombreLenguaje



class Reclutador(models.Model):
    empresa = models.CharField(max_length=255)
    lugarEmpresa = models.CharField(max_length=255)
    primera = models.PositiveIntegerField(default=0)
    usuario = models.OneToOneField(User)

    def __str__(self):
	       return self.usuario.username


class Organizador(models.Model):
    primera = models.PositiveIntegerField(default=0)
    usuario = models.OneToOneField(User)

    def __str__(self):
	       return self.usuario.username


class Coder(models.Model):
    github = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    lugarVive = models.CharField(max_length=255, default="")
    primera = models.PositiveIntegerField(default=0)

    remoto = '1'
    presencial = '2'
    dispone = (
        (remoto, 'remoto'),
        (presencial, 'presencial')
    )
    disponibilidad = models.CharField(max_length=255, choices=dispone, default=presencial)

    completo = '1'
    medio = '2'
    t = (
        (completo, 'completo'),
        (medio, 'medio tiempo'),
    )
    tiempo = models.CharField(max_length=255, choices=t, default=completo)

    usuario = models.OneToOneField(User)

    def __str__(self):
	       return self.usuario.username


class Equipos(models.Model):
    nombreEquipo = models.CharField(max_length=255)
    nombreProyecto = models.CharField(max_length=255)
    descripcionProyecto = models.TextField(default="None")
    participantes = models.ManyToManyField(Coder)
    tecnologias = models.ManyToManyField(Lenguaje)

    def __str__(self):
	       return self.nombreEquipo
