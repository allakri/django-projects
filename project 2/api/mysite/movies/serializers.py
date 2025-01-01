from rest_framework import serializers
from .models import moviesdata

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = moviesdata
        fields = ['id', 'name', 'rating', 'duration','typ','image']