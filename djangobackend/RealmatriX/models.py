from django.db import models


class properties(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    type = models.CharField(max_length = 255)
    status = models.CharField(max_length = 255)
    size = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()



