from typing import no_type_check

from django.contrib.postgres.indexes import GinIndex, OpClass
from django.db import models

from apps.autor.models import Autor

from .managers import CategoryManager, LibroManager


# Create your models here.
class Categoria(models.Model):
    name = models.CharField('Category name', max_length=30)

    objects = CategoryManager()

    def __str__(self):
        return f'{self.id} - {self.name}'

class Libro(models.Model):
    category = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name='category_libro'
    )
    autores = models.ManyToManyField(Autor)
    title = models.CharField('Title book', max_length=50)
    date = models.DateField('Published date', auto_now=False, auto_now_add=False)
    cover_page = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,null=True,blank=True)
    visit_num = models.PositiveIntegerField()
    stoke = models.PositiveIntegerField(default=0)
    objects = LibroManager()
        

    def __str__(self):
        return f'{self.id} - {self.title}'
