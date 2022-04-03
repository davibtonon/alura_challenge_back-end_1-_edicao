from django.shortcuts import render
from videos_api.models import Video, Categoria
from videos_api.serializers import VideoSerializers, CategoriaSerializers, ListaVideosCategoriasSerializers
from rest_framework import viewsets, generics
# Create your views here.

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

class CategoriasViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class ListaVideosCategorias(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaVideosCategoriasSerializers