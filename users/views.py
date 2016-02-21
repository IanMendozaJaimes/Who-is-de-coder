from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Coder, Reclutador
from django.http import JsonResponse


def loginView(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'registro.html', {})

def resultadosView(request):
    busqueda = request.POST['keyword']
    return render(request, 'resultados.html', {'busqueda':busqueda})


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
    github = False
    linkedin = False
    que = 0
    existe = None
    user = None
    si = 0
    nombre = request.user.first_name
    nickname = request.user.username

    try:
        user = User.objects.get(username=nickname)
        existe = Coder.objects.get(usuario=user)
        que = request.session.get('quees')


        if existe.primera != 0:
            si = 1
            github = existe.github
            linkedin = existe.linkedin

        if que != 1:
            request.session["quees"] = 1
            que = 1

        return render(request, 'coders.html', {'nickname':nickname, 'nombre':nombre, 'esCoder':si, 'queEs': que, 'github':github, 'linkedin':linkedin})
    except Exception as e:
        que = 1
        return render(request, 'coders.html', {'nickname':nickname, 'nombre':nombre, 'esCoder':si, 'queEs': que, 'github':github, 'linkedin':linkedin})


def reclutadorView(request):
    nombre = request.user.first_name
    nickname = request.user.username
    empresa = False
    lugarEmpresa = False
    que = 0
    existe = None
    user = None
    si = 0

    try:
        user = User.objects.get(username=nickname)
        existe = Reclutador.objects.get(usuario=user)
        que = request.session.get('quees')

        if existe.primera != 0:
            si = 1
            empresa = existe.empresa
            lugarEmpresa = existe.lugarEmpresa

        if que != 3:
            request.session["quees"] = 3
            que = 3
            si = 1

        return render(request, 'reclutador.html', {'nickname':nickname, 'nombre':nombre, 'esReclutador':si, 'queEs': que, 'empresa':empresa, 'lugarEmpresa':lugarEmpresa})

    except Exception as e:
        que = 3
        return render(request, 'reclutador.html', {'nickname':nickname, 'nombre':nombre, 'esReclutador':si, 'queEs': que, 'empresa':empresa, 'lugarEmpresa':lugarEmpresa})

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
    nickname = request.user.username
    empresa = request.POST['empresa']
    lugarEmpresa = request.POST['lugarEmpresa']
    primera = 1

    usuario = User.objects.get(username=nickname)
    reclutador = Reclutador(usuario=usuario, empresa=empresa, lugarEmpresa=lugarEmpresa, primera=primera)
    reclutador.save()

    return render(request, 'reclutador.html', {})
