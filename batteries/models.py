from django.db import models


class Battery(models.Model):
    name = models.CharField(max_length=200)
    max_volts = models.DecimalField('Max voltage, V', max_digits=7, decimal_places=4)
    min_volts = models.DecimalField('Min voltage, V', max_digits=7, decimal_places=4)
    capacity = models.DecimalField('standard capacity, Ah', max_digits=7, decimal_places=4)

    def __str__(self):
        return self.name


class BatteryState(models.Model):
    battery = models.ForeignKey(Battery)
    timestamp = models.DateTimeField('state timestamp', auto_now=True)
    voltage = models.DecimalField('measured voltage, V', max_digits=7, decimal_places=4)
    capacity_state = models.DecimalField('Percent capacity', max_digits=5, decimal_places=4,default=1)

    def __str__(self):
        return str(self.timestamp)
