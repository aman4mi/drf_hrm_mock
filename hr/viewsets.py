from rest_framework import viewsets
from . import models
from . import serializers

class CountryViewsets(viewsets.ModelViewSet):
      queryset = models.Country.objects.all()
      serializer_class = serializers.CountrySerializers

class CityViewsets(viewsets.ModelViewSet):
      queryset = models.City.objects.all()
      serializer_class = serializers.CitySerializers

class OrganizationViewsets(viewsets.ModelViewSet):
      queryset = models.Organization.objects.all()
      serializer_class = serializers.OrganizationSerializers