from django.shortcuts import render
from rest_framework import generics
# Create your views here.
def home(request):
    return render(request, 'begin.html', {})

class HackatonList(generics.ListCreateAPIView):
    queryset = Hackaton.objects.all()