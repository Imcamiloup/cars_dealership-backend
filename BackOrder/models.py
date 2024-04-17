from django.db import models


# Create your models here.
class BackOrder(models.Model):
    brand = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    aspirant = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Brand
        