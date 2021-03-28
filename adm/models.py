from django.db import models


class Modulo(models.Model):
    nome = models.CharField(max_length=30, default='')
    descricao = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=30, default='')
    dt_criacao = models.CharField(max_length=10, default='')
    descricao = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.nome


class Estudante(models.Model):
    nome = models.CharField(max_length=30, default='')
    cpf = models.CharField(max_length=9, default='')
    telefone = models.CharField(max_length=11, default='')
    nota = models.CharField(max_length=3, default='')
    falta = models.CharField(max_length=3, default='')
    status = models.CharField(max_length=1, default='')

    def __str__(self):
        return self.nome
