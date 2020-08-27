from rest_framework import viewsets
from . import models
from . import serializers

class SongsViewsets(viewsets.ModelViewSet):
      queryset = models.Songs.objects.all()
      serializer_class = serializers.SongsSerializer