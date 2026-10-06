from django.contrib import admin
from .models import Livro, Autor

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'data_lancamento')
    search_fields = ('titulo', 'editora')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'ano_nascimento')
    search_fields = ('nome', 'email')