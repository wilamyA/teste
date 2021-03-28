from rest_framework import serializers
from adm.models import Estudante, Modulo, Turma


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'cpf', 'telefone','nota', 'falta', 'status']


class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ['id', 'nome', 'descricao']


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['id', 'nome', 'descricao', 'dt_criacao']
