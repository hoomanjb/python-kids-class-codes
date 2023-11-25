from django.shortcuts import render

# Create your views here. test.com/countries

from rest_framework import viewsets

from .models import Country
from .serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
