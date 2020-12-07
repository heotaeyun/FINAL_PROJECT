from rest_framework import serializers
from .models import Movies

class PopularSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ['id', 'title', 'rate', 'img_url', 'story']


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ['title', 'rate', 'story','genre', 'img_url']