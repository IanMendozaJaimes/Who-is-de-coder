from django.db import models
from django.contrib.auth.models import User
from users.models import Coder


class Equipos(models.Model):
    nombreEquipo = models.CharField(max_length=255)
    nombreProyecto = models.CharField(max_length=255)
    descripcionProyecto = models.TextField(default="None")
    participantes = models.ManyToManyField(Coder)


class Hackaton(models.Model):
    nombreHackaton = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)
    descripcion = models.TextField(default="None")
    fecha = models.DateTimeField(auto_now=False)
    equipos = models.ManyToManyField(Equipos)
