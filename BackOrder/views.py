from rest_framework import viewsets
from .serializer import carsWaitListSerializer
from .models import CarsWaitList

# Create your views here.
class carsWaitListView(viewsets.ModelViewSet):
    serializer_class =  carsWaitListSerializer
    queryset = CarsWaitList.objects.all()