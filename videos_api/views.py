from videos_api.models import Video, Categoria
from videos_api.serializers import VideoSerializers, CategoriaSerializers, ListaVideosCategoriasSerializers
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers


class CategoriasViewset(viewsets.ModelViewSet):
    """Exibir todas as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers
    #Adiciona o filtros na API
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']
    http_method_names = ['get', 'post', 'put']
    

class ListaVideosCategorias(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaVideosCategoriasSerializers