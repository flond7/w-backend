from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render

from .serializer import womanSerializer
from .models import woman


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
  basicApi_urls = {
    'List':'/woman-list/',
    'Detail':'/woman-detail/<str:pk>',
    'Create':'/woman-create/',
    'Update':'/woman-update/<str:pk>',
    'Delete':'/woman-delete/<str:pk>',
  }
  return Response(basicApi_urls)

@api_view(['GET'])
def womanList(request):
  w = woman.objects.all()
  serializer = womanSerializer(w, many=True)  # many=true returns more objects
  return Response (serializer.data)

@api_view(['GET'])
def womanDetail(request, pk):
  w = woman.objects.get(id=pk)
  serializer = womanSerializer(w, many=False) # many=false returns one object
  return Response (serializer.data)

@api_view(['POST'])
def womanCreate(request):
  serializer = womanSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['POST'])
def womanUpdate(request, pk):
  w = woman.objects.get(id=pk)
  serializer = womanSerializer(instance=w, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['DELETE'])
def womanDelete(request, pk):
  w = woman.objects.get(id=pk)
  w.delete()
  return Response ("Item deleted")

