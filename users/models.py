from django.db import models
from django.contrib.auth.models import User

class Reclutador(models.Model):
    empresa = models.CharField(max_length=255)
    lugarEmpresa = models.CharField(max_length=255)


class Lenguaje(models.Model):
    nombreLenguaje = models.CharField(max_length=255)
