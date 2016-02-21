from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Coder
from django.http import JsonResponse


def loginView(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'registro.html', {})


def registroUser(request):
    nom = request.POST['nombreName']
    email = request.POST['emailName']
    contra = request.POST['contraName']

#    existe = User.objects.all()
#    si = False
#    for e in existe:
#        if e.username == nom:
#            si = True

    try:
        user = User.objects.create_user(username=nom,  password=contra)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.email = email
        user.save()
        login(request, user)
        request.quees = 0
    except Exception as e:
        return redirect('/user/signup/')

    return redirect('/home')


def loginUser(request):
    nom = request.POST['nombreName']
    contra = request.POST['contraName']
    user = User.authenticate(username=nom, password=contra)

    if user is not None:
        if user.is_active:
            login(user)
            request.quees = 0
            return render(request, 'begin.html', {nombre:user.username})
        else:
            return redirect('/login')


def coderView(request):
    nombre = request.user.username
    existe = User.objects.get(username=nombre)
    si = False
    if existe is not None:
        si = True

    if request.quees == 0:
        request.quees = 1;

    return render(request, 'coders.html', {nombre:nombre, esCoder:si, queEs: request.quees})

def crearCoder(request):
    nombre = request.user.username
    github = request.POST['githubName']
    linkedin = request.POST['linkedinName']
    nickname = request.POST['nicknameName']
    lugarVive = request.POST['lugarViveName']
    primera = 1
    disponibilidad = request.POST['disponibilidadName']
    tiempo = request.POST['tiempoName']

    coder = Coder(github, linkedin, nickname, lugarVive, primera, disponibilidad, tiempo)
    coder.save()

    return JsonResponse({creado:True})


# 0 es nada
# 1 es coder
# 2 es organizador
# 3 es reclutador
