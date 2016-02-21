from django.shortcuts import render
from .models import Hackaton
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
