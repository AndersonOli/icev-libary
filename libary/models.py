from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField("Título do Livro", max_length=250)
  author = models.CharField("Autor", max_length=250)
  num_pages = models.IntegerField("Número de páginas")
  description = models.CharField("Descrição", max_length=250)
  year_launched = models.CharField("Ano de lançamento", max_length=250)
