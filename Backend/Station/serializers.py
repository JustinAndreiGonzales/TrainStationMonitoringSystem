from rest_framework import serializers
from .models import Station, HourlyDensity, DailyDensity

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class HourlyDensitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyDensity
        fields = '__all__'


class DailyDensitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyDensity
        fields = '__all__'
