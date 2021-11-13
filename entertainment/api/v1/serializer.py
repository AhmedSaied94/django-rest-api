from django.db.models.base import Model
from rest_framework import fields, serializers
from entertainment.models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'

class SeissonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seisson
        fields = '__all__'

class EposideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eposides
        fields = '__all__'

class CatigorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catigorie
        fields = '__all__'