from django.db import models


class InfinityStones(models.Model):
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=10)
    description = models.TextField(max_length=250)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.name
