from rest_framework import serializers
from .models import BackOrder

class backOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackOrder
        fields = ['id', 'brand', 'site', 'aspirant']


        