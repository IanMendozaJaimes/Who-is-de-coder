from django.shortcuts import render
from .models import Hackaton
from rest_framework import generics
from users.models import Equipos, Coder, Lenguaje
from .serializers import TechListSerializer, EquipoDetailSerializer, HackatonSerializer, EquipoSerializer, HackatonDetailSerializer, EquiposBusqueda, SponsorsListSerializer
from django.contrib.auth.decorators  import  login_required
# Create your views here.


@login_required(login_url='/user/login')
def home(request):
    return render(request, 'begin.html', {'username':request.user.username, 'nombre':request.user.first_name})


def index(request):
    return render(request, 'index.html', {})

def hackatones(request, idHackaton):
    return render(request, 'hackaton.html', {'idHackaton': idHackaton})


class HackatonList(generics.ListCreateAPIView):
    queryset = Hackaton.objects.all()
    serializer_class = HackatonSerializer

class HackatonListUser(generics.ListCreateAPIView):
    serializer_class = HackatonSerializer

    def get_queryset(self):
        hackatones = []
        equipos = []
        username = self.kwargs.get('username')
        try:
            usuario = Coder.objects.get(usuario__username=username).id
            if usuario:
                equipos = Equipos.objects.filter(participantes__usuario=usuario)
                for equipo in equipos:
                    hackatones = Hackaton.objects.filter(equipos__id=equipo.id)
        except:
            return hackatones

        return hackatones


class HackatonEquiposList(generics.ListAPIView):
    serializer_class = EquipoSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        hackaton = Hackaton.objects.get(id=id)
        equipos = hackaton.equipos.all()

        return equipos


class EquiposBusquedaView(generics.ListAPIView):
    serializer_class = EquiposBusqueda

    def get_queryset(self):
        tecno = self.kwargs.get('parametro')
        t = Lenguaje.objects.get(nombreLenguaje=tecno)
        equipos = Equipos.objects.filter(tecnologias=t)

        return equipos


class HackatonDetail(generics.RetrieveAPIView):
    queryset = Hackaton.objects.all()
    serializer_class = HackatonDetailSerializer
    lookup_field = 'id'

class SponsorsList(generics.ListAPIView):
    serializer_class = SponsorsListSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        hackaton = Hackaton.objects.get(id=id)
        equipos = hackaton.sponsores.all()

        return equipos

class EquipoDetail(generics.RetrieveAPIView):
    queryset = Equipos.objects.all()
    serializer_class = EquipoDetailSerializer
    lookup_field = 'id'

class TechList(generics.ListAPIView):
    serializer_class = TechListSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        equipos = Equipos.objects.get(id=id)
        techs = equipos.tecnologias.all()

        return techs