from rest_framework import serializers
from .models import Movies


class MovivesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Movies
        fields = '__all__'