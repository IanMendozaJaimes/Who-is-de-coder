from django.db import models
from django.contrib.auth.models import User
from users.models import Organizador, Equipos


class Hackaton(models.Model):
    nombreHackaton = models.CharField(max_length=255)
    lugar = models.CharField(max_length=255)
    descripcion = models.TextField(default="")
    fecha = models.DateTimeField(auto_now=False)
    equipos = models.ManyToManyField(Equipos)
    organizadores = models.ManyToManyField(Organizador)
