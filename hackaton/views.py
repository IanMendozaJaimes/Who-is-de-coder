from django.shortcuts import render
from .models import Hackaton
from rest_framework import generics
from .serializers import HackatonSerializer
# Create your views here.
def home(request):
    return render(request, 'begin.html', {'nombre':request.user.username})

class HackatonList(generics.ListCreateAPIView):
    queryset = Hackaton.objects.all()
    serializer_class = HackatonSerializer

def prueba(request):
    return render(request, 'prueba.html', {})
