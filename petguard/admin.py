from django.contrib import admin
from .models import Animal, Especie, Raca


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especie')
    list_filter = ('especie',)
    search_fields = ('nome',)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'especie', 'raca', 'anos', 'meses', 'status')
    list_filter = ('status', 'especie', 'raca')
    search_fields = ('raca__nome', 'especie__nome')
