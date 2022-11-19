from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
@api_view(['GET'])
def create(request):
    serializer = ItemSerializer(request.data)
    return Response({
        "data": serializer
    })

