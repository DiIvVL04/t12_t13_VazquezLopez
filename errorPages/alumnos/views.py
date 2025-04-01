from .models import Alumno
from .serializers import AlumnoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .forms import alumnoForm
from django.shortcuts import render

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]

def agregar_alumno(request):
    form = alumnoForm()
    return render(request,'agregar2.html',{'form':form})