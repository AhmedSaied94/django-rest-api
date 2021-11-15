from django.db.models.base import Model
from rest_framework import fields, serializers
from entertainment.models import *




class NewRepresent(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


        
class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class CatigorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catigorie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    casts = NewRepresent(many=True)
    catigories = NewRepresent(many=True)
    # uploaded_by = NewRepresent(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
        # depth = 1
        



class SeriesSerializer(serializers.ModelSerializer):
    casts = serializers.StringRelatedField(many=True)
    catigories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Series
        fields = '__all__'

class SeissonSerializer(serializers.ModelSerializer):
    series = serializers.StringRelatedField()
    class Meta:
        model = Seisson
        fields = '__all__'

class EposideSerializer(serializers.ModelSerializer):
    seisson = serializers.StringRelatedField()
    class Meta:
        model = Eposides
        fields = '__all__'

