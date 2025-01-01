from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import moviesdata 
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = moviesdata.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = moviesdata.objects.filter(typ='action')
    serializer_class = MovieSerializer