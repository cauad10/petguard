from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Animal, Especie, Raca

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

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
