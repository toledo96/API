from rest_framework import routers, serializers, viewsets
from myapi.models import Alumno


class AlumnoSerializers(serializers.ModelSerializer):
    #denuncias = serializers.SlugRelatedField(many=True,read_only=True,slug_field='titulo')
    #denuncias =serializers.SlugRelatedField(many=True,read_only=True,slug_field='descripcion')
    #denuncias =serializers.StringRelatedField(many=True)
    #no sirvio denuncias= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Alumno
        fields = ('__all__')