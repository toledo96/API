from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from myapi import views

urlpatterns = [
     re_path(r'^alumno_lista/$', views.AlumnoLista.as_view() ),
     re_path(r'^alumno_detalles/(?P<id>\d+)$', views.AlumnoDetalles.as_view() ),   
]

