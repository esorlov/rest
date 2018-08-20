from django.contrib import admin
from .models import Battery, BatteryState


admin.site.register(Battery)
admin.site.register(BatteryState)
