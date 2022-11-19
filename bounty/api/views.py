from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def getElements(request):

    return Response({
        "ok":"done"
    })

@api_view(['POST'])
def addElements(request):
    data = request.data
    return Response({
        "data":data
    })


