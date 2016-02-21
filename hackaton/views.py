from django.shortcuts import render
from .models import Hackaton
from users.models import Equipos
from rest_framework import generics
from .serializers import HackatonSerializer
from django.contrib.auth.decorators  import  login_required
# Create your views here.


@login_required(login_url='/user/login')
def home(request):
    return render(request, 'begin.html', {'username':request.user.username, 'nombre':request.user.first_name})


def index(request):
    return render(request, 'index.html', {})


class HackatonList(generics.ListCreateAPIView):
    queryset = Hackaton.objects.all()
    serializer_class = HackatonSerializer

class HackatonListUser(generics.ListCreateAPIView):
    def get_queryset(self):
        username = self.request.get('id')

    equipos = Equipos.objects.filter(participantes__id=id)