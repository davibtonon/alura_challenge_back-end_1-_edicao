from videos_api.models import Video, Categoria
from videos_api.serializers import VideoSerializers, CategoriaSerializers, ListaVideosCategoriasSerializers
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CategoriasViewset(viewsets.ModelViewSet):
    """Exibir todas as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

    #Adiciona o filtros na API
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']
    http_method_names = ['get', 'post', 'put']

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class ListaVideosCategorias(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListaVideosCategoriasSerializers

class ListaVideosFree(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.filter(free=True)

        return queryset

    serializer_class = VideoSerializers