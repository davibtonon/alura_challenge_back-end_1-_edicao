from rest_framework import serializers
from videos_api.models import Video, Categoria


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titulo', 'descricao', 'url', 'categoria']


class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'titulo', 'cor']


class ListaVideosCategoriasSerializers(serializers.ModelSerializer):
    """Lista de Videos por categoria"""
    class Meta:
        model = Video
        fields = ['titulo']

