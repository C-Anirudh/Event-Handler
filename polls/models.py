from django.db import models


class Polls(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
