from django.db import models
from django.urls import reverse
from administrator.models import SuggestedEvents


class Polls(models.Model):
    event_name = models.ForeignKey(
        SuggestedEvents.name, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('poll')
