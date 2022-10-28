# Usado para tratar as informações dos filmes que se encontra no arquivo 'movies_metadata.csv"
# Esse script é utilizado para add informações na API para realização de teste.

import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challenge_back_end_1.settings')
django.setup()

import linecache
import ast
from random import randint, choices
from faker import Faker
from videos_api.models import Categoria, Video
from django.core.exceptions import ObjectDoesNotExist

CORES = [ 
    "Azul", "Verde", "Amarelo", "Roxo", "Rosa", 
    "Vermelho", "Laranja", "Marrom", "Cinza", "Branco",	"Preto"
    ]


def pegar_categoria(categorias):
    try:
        categorias = ast.literal_eval(categorias)
        total_categorias = len(categorias) - 1
        escolher_uma_categoria = randint(0, total_categorias)
        try:
            return categorias[escolher_uma_categoria]['name']
        except:
            return categorias['name']

    except:
        print(categorias)
  

def pegar_nome_descricao_filme(filme):
    final_lista_categorias = filme.find(']')
    final_nome_filme = filme[final_lista_categorias + 2:].find(',')
    inicio_descricao_filme = final_lista_categorias + final_nome_filme + 3

    nome_filme = filme[final_lista_categorias + 2:]
    nome_filme = nome_filme[:final_nome_filme]
    descricao_filme = filme[inicio_descricao_filme:]
    
    return nome_filme, descricao_filme


def dados_filme():
    numero_filme = randint(1, 45570)
    filme = linecache.getline('movies_metadata.csv', numero_filme)
    final_lista_categorias = filme.find(']')
    lista_categorias = filme[1:final_lista_categorias]
    
    nome, descricao = pegar_nome_descricao_filme(filme)
    filme_categoria = pegar_categoria(lista_categorias)
    cor = choices(CORES)[0]
    procura_filme = Video.objects.filter(titulo=nome)
    
    try:
        nova_categoria = Categoria.objects.get(titulo=filme_categoria)
    except ObjectDoesNotExist:
        nova_categoria = Categoria(titulo=filme_categoria, cor=cor)
        nova_categoria.save()

    if not procura_filme:
        cadastrar_novo_filme = Video(
            titulo=nome,
            descricao=descricao[:250],
            url=Faker().image_url(),
            categoria=nova_categoria
            )
        cadastrar_novo_filme.save()

def main(qti):
    for _ in range(qti):
        dados_filme()
    

main()