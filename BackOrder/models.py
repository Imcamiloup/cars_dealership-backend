from django.db import models


# Create your models here.
class BackOrder(models.Model):
    Brand = models.CharField(max_length=100)
    Site = models.CharField(max_length=100)
    Aspirant = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Brand
        