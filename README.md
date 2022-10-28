# Alura Challenge Back-end 1º edição

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20CONCLUIDO&color=GREEN&style=for-the-badge)

## Descrição do projeto 

<p align="justify">
  Criação de uma API Rest para o compartilhamento de videos,com o objetivo de praticar e ganhar experiencia na área de desenvolvimento back-end.

  A plataforma deve permitir ao usuário montar playlists com links para seus vídeos preferidos, separados por categorias.
</p>


# Funcionalidades do API

:heavy_check_mark: Cadastros de videos. 

:heavy_check_mark: Cadastros de categorias

:heavy_check_mark: Filtros por nomes e categorias de videos.

:heavy_check_mark: Autenticação de usuarios.

## Layout ou Deploy da Aplicação :dash:


## Pré-requisitos

:warning: [Python](https://www.python.org/)

:warning: [Django](https://www.djangoproject.com/)

:warning: [Django-rest-framework](https://www.django-rest-framework.org/)


## Como rodar a aplicação :arrow_forward:

No terminal, clone o projeto:

```
git clone hhttps://github.com/davibtonon/alura_challenge_back-end_1-_edicao.git
```

Caso deseje cria um ambiente virtual digite o comandao abaixo no terminal:

```#python
python -m venv venv 
```

Para ativa o ambiente virtual digite:

```#shell
source /venv/bin/activate
```

Instale todas as dependências do arquivo requiremenst.txt com o camando abaixo:

```#python
python -m pip install -r requirements.txt
```

**Para mais informações veja ->** [pip](https://pip.pypa.io/en/stable/user_guide/).

Em seguida digite o comando abaixo para inicia o servidor:

``` python
python manage.py runserver
```

Caso deseje inserir dados para teste execute o arquivo *filmes_seed*:

``` python
python filmes_seed.py
```

Abra o navegador no endereço abaixo e teste o sistema.:

``` python
 http://127.0.0.1:8000/
```

## Guia Utilização da API.

### GET */videos*

- Response 200 (json):

  > **id:** 1,<br>
    **titulo:** "Requisisdfsadfção Patch",<br>
    **descricao:** "dffsadfsadfasasdfas",<br>
    **url:** "http://www.example.com.br",<br>
    **categoria**": 2**,<br>
    **free:** true

### PUT */videos/id*

- Atualizar as informações de um vídeo de acordo com id.

### DELETE */videos/id*

- Deleta um video.

### DELETE */videos/free*

- Retorna todos só videos gratuito da plataforma

### GET */categorias*

- Retorna com as informações das categorias:

  > **id:** 1,<br>
    **titulo:** "comedia",<br>
    **cor:** "dffsadfsadfasasdfas",<br>

### PUT */categorias/id*

- Retorna com as informações de uma categoria.

### GET */categorias/id/videos*

- Filtra os videos por categorias.

### DELETE */categorias/id*

- Deleta uma categoria.

## Desenvolvedores/Contribuintes :octocat:
[Davi B Tonon](https://github.com/davibtonon)