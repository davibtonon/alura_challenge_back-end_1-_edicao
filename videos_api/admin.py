from django.contrib import admin
from videos_api.models import Video
# Register your models here.

class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')

admin.site.register(Video, Videos)