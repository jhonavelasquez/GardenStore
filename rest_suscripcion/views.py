from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Suscripcion
from rest_suscripcion.serializers import SuscripcionSerializers

@csrf_exempt
@api_view(['GET','POST'])
def lista_suscripcion(request):
    if request.method == 'GET':
        suscripcion = Suscripcion.objects.all()
        serializer = SuscripcionSerializers(suscripcion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SuscripcionSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def datalle_suscripcion(request, id):
    try:
        suscripcion = Suscripcion.objects.get(nombre=id)
    except Suscripcion.Does.NotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SuscripcionSerializers(suscripcion)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SuscripcionSerializers(suscripcion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        suscripcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)