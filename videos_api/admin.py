from django.contrib import admin
from videos_api.models import Video, Categoria
# Register your models here.

class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cor')

admin.site.register(Video, Videos)
admin.site.register(Categoria, Categorias)