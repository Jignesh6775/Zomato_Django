from django.db import models

# Create your models here.


class Order(models.Model):
    foodname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
