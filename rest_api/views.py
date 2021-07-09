from django.shortcuts import render
from core.models import Juego
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_api.serializers import JuegoSerializer
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def lista_juego(request):
    """
    Lista todos los juegos
    """
    if request.method == 'GET':
        juego = Juego.objects.all()
        serializer = JuegoSerializer(juego, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JuegoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def detalle_juego(request, id):
    """
    Traer elemto de la base de datos
    """

    try:
        juego = Juego.objects.get(id=id)
    except Juego.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = JuegoSerializer(juego)
        return Response(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = JuegoSerializer(juego, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
    elif request.method == 'DELETE':
        juego.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)