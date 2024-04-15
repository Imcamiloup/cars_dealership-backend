from rest_framework import serializers
from .models import CarsWaitList

class carsWaitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsWaitList
        fields = ['id', 'brand', 'site', 'aspirant']
        
        
        