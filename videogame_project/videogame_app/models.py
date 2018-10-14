from django.db import models
from django.utils import timezone

class GameIdea(models.Model):
    name=models.CharField(max_length=100)
    genre= models.CharField(max_length=100)

    currentdate= models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name, self.genre

    def displayed(self):
        self.currentdate = timezone.now()
        self.save()