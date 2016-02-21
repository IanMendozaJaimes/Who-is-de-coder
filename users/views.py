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
    nick = request.POST['nickName']

#    existe = User.objects.all()
#    si = False
#    for e in existe:
#        if e.username == nom:
#            si = True

    try:
        user = User.objects.create_user(username=nick,  password=contra)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.email = email
        user.first_name = nom
        user.save()
        login(request, user)
        request.session['quees'] = 0
    except Exception as e:
        return redirect('/user/signup/')

    return redirect('/home')


def loginUser(request):
    nom = request.POST['nickName']
    contra = request.POST['contraName']
    user = authenticate(username=nom, password=contra)

    if user is not None:
        if user.is_active:
            login(request, user)
            request.session["quees"] = 0
            return redirect('/home')
        else:
            return redirect('/user/login')

    else:
        return redirect('/user/login')


def coderView(request):
    nombre = request.user.first_name
    nickname = request.user.username
    github = False
    linkedin = False
    que = 0
    existe = None
    user = None
    si = 0

    try:
        user = User.objects.get(username=nickname)
        existe = Coder.objects.get(usuario=user)
        que = request.session.get('quees')

        if existe.primera != 0:
            si = 1
            github = existe.github
            linkedin = existe.linkedin

        if que == 0:
            request.session["quees"] = 1
            que = 1

        return render(request, 'coders.html', {'nickname':nickname, 'nombre':nombre, 'esCoder':si, 'queEs': que, 'github':github, 'linkedin':linkedin})
    except Exception as e:
        que = 1
        return render(request, 'coders.html', {'nickname':nickname, 'nombre':nombre, 'esCoder':si, 'queEs': que, 'github':github, 'linkedin':linkedin})


def reclutadorView(request):
    return render(request, 'reclutador.html', {})


def crearCoder(request):
    nombre = request.user.first_name
    github = request.POST['Github']
    linkedin = request.POST['Linkedin']
    nickname = request.user.username
    lugarVive = request.POST['Lugar']
    primera = 1
    disponibilidad = request.POST['Presencial']
    tiempo = request.POST['Tiempo']

    usuario = User.objects.get(username=nickname)
    coder = Coder(github=github, linkedin=linkedin, usuario=usuario, lugarVive=lugarVive, primera=primera, disponibilidad=disponibilidad, tiempo=tiempo)
    coder.save()

    return render(request, 'coders.html', {})


# 0 es nada
# 1 es coder
# 2 es organizador
# 3 es reclutador


def crearReclutador(request):
    nombre = request.user.username
