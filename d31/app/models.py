from django.db import models


class Play(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    he = models.IntegerField(default=170)
    pop = models.IntegerField(default=100)

