from urllib import response
from django.test import TestCase
from django.urls import reverse
from rest_framework import status # Retorna os status das requições HTTP
from videos_api.models import Categoria, Video
# Create your tests here.

class CategoriaTestCase(TestCase):

    def setUp(self) -> None:
        
        self.list_url = reverse('Categorias-list')
        self.categoria_drama_teste = Categoria.objects.create(
            titulo='Drama', cor='Amarelo')
        self.cateogira_ficcao_teste = Categoria.objects.create(
            titulo='ficao', cor='Azul')

    def test_requisicao_get_lista_categorias(self):
        """Teste para testa a requisicao GET da categorias"""
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_cria_categoria(self):
        """Teste para requisição POST categoria"""
       
        data = {'titulo': 'Aventura', 'cor': 'verde'}
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_para_deleta_categoria(self):
        """Teste requisição para deleta categoria"""
        
        response = self.client.delete('/categorias/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_para_atualizar_categoria(self):
        """Teste para requisicao PUT"""
        pass
        # data = {
        #     'titulo':'ficção', 
        #     'cor':'Vermelho'
        #     }

        # response = self.client.put('/categorias/1/', data=data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)