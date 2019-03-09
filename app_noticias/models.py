from django.db import models

class Noticia(models.Model):
    titulo = models.CharField("Título", max_length=128)
    conteudo = models.TextField()
    data_cria = models.DateTimeField('Data criação')
    data_pub = models.DateField(auto_now=True)
    publicado = models.BooleanField()

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    def __str__(self):
        return self.titulo
