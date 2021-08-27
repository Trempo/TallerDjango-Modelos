from django.db import models
from measurements.models import Measurement


class Alarm(models.Model):
    measurements = models.ManyToManyField(Measurement)
    status = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.status)
