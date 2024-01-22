from django.db import models


class properties(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    type = models.CharField(max_length = 255)
    status = models.CharField(max_length = 255)
    size = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()


class users(models.Model):
    name=models.CharField(max_length=255)  
    email=models.CharField(max_length=255)  
    nic=models.CharField(max_length=255)  
    role=models.CharField(max_length=255)  
    phoneno=models.IntegerField()  
    address=models.CharField(max_length=255)  



