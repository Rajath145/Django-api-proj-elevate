from rest_framework import serializers
from .models import movies

class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model=movies
        fields="__all__"
