from rest_framework import viewsets
from adm.models import Estudante, Modulo, Turma
from adm.serializer import EstudanteSerializer, ModuloSerializer, TurmaSerializer


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class ModulosViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class TurmasViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
