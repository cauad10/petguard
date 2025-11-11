from django.contrib import admin
from .models import Animal, Especie


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'especie', 'raca', 'anos', 'meses', 'status')
    list_filter = ('status', 'especie')
    search_fields = ('raca',)


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
