from rest_framework import serializers
from . import models


class BatterySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','name', 'max_volts', 'min_volts', 'capacity',)
        model = models.Battery


class BatteryStateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'battery', 'timestamp', 'voltage',)
        model = models.BatteryState