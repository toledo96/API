from django.shortcuts import render
from myapi.models import Alumno
from myapi.serializer import AlumnoSerializers
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import Http404

class AlumnoLista(APIView):
    
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delete=False)
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AlumnoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlumnoDetalles(APIView):
    def get_object(self, id):
        try:
            return Alumno.objects.get(pk=id, delete=False)
        except Alumno.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        usuario = self.get_object(id)
        if usuario != False:
            serializer = AlumnoSerializers(usuario)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Alumno.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        usuario = self.get_object(id)
        if usuario != False:
            serializer = AlumnoSerializers(usuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
