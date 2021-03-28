from django.contrib import admin
from adm.models import Estudante, Turma, Modulo


class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


class Turmas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


class Modulos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Estudante, Estudantes)
admin.site.register(Turma, Turmas)
admin.site.register(Modulo, Modulos)
