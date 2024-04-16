from .serializer import backOrderSerializer
from .models import BackOrder
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404



# Create your views here.
class BackOrderList(APIView):

    def get(self, request, format=None):
        backorders = BackOrder.objects.all()
        serializer = backOrderSerializer(backorders, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = backOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class BackOrderDetail(APIView):
    def get_object(self, pk):
        try:
            return BackOrder.objects.get(pk=pk)
        except BackOrder.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        backorder = self.get_object(pk)
        serializer = backOrderSerializer(backorder)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        backorder = self.get_object(pk)
        serializer = backOrderSerializer(backorder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk, format=None):
        backorder = self.get_object(pk)
        backorder.delete()
        return Response(status=204)    
    
