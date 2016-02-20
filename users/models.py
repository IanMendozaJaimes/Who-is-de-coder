from django.db import models
from django.contrib.auth.models import User
from hackaton.models import Hackaton


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



class Reclutador(models.Model):
    empresa = models.CharField(max_length=255)
    lugarEmpresa = models.CharField(max_length=255)
    lenguajes = models.ManyToManyField(Lenguaje)
    usuario = models.OneToOneField(User)


class Organizador(models.Model):
    hackatones = models.ManyToManyField(Hackaton)
    usuario = models.OneToOneField(User)


class Coder(models.Model):
    github = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    lugarVive = models.CharField(max_length=255)

    remoto = 'remoto'
    presencial = 'presencial'
    dispone = (
        (remoto, 'remoto'),
        (presencial, 'presencial')
    )

    disponibilidad = models.CharField(max_length=255, choices=dispone, default=presencial)

    usuario = models.OneToOneField(User)
