from django.shortcuts import render
from rest_framework import generics

from .models import Battery, BatteryState
from .serializers import BatterySerializer, BatteryStateSerializer


class BatteryList(generics.ListCreateAPIView):
    queryset = Battery.objects.all()
    serializer_class = BatterySerializer


class BatteryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Battery.objects.all()
    serializer_class = BatterySerializer


class BatteryStateList(generics.ListCreateAPIView):
    queryset = BatteryState.objects.all()
    serializer_class = BatteryStateSerializer


class BatteryStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BatteryState.objects.all()
    serializer_class = BatteryStateSerializer

