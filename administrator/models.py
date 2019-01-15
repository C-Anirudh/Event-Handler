from django.db import models
from django.utils import timezone
from django.urls import reverse


class EventDetails(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.CharField(max_length=200)
    event_date = models.DateTimeField(default=timezone.now())
    fee = models.FloatField(default=0)
    last_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('addevent')
