from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class AboutViewset(viewsets.ModelViewSet):
    queryset = models.About.objects.all()
    serializer_class = serializers.AboutSerializer

