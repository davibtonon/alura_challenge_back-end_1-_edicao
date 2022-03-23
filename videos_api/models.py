from django.db import models

# Create your models here.

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    url = models.URLField()

    def __str__(self) -> str:
        return self.titulo