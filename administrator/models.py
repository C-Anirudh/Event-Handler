from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class EventDetails(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.CharField(max_length=200)
    event_date = models.DateTimeField(default=timezone.now())
    fee = models.FloatField(default=0)
    last_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard')


class SuggestedEvents(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    feasible_event_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('dashboard')

    def __str__(self):
        return self.name


class Registrants(models.Model):
    event = models.ForeignKey(
        EventDetails, on_delete=models.CASCADE, null=True, blank=False)
    roll = models.CharField(max_length=200, null=True,
                            blank=False)

    def get_absolute_url(self):
        return reverse('dashboard')
