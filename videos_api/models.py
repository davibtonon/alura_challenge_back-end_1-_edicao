from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    cor = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.titulo

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    url = models.URLField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.titulo