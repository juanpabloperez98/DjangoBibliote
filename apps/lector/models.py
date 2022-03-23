from django.db import models
from apps.libro.models import Libro
from .managers import PrestamoManager


# Create your models here.
class Lector(models.Model):
    name = models.CharField('Reader name', max_length=50)
    last_name = models.CharField('Reader last name', max_length=50)
    nacionality = models.CharField('Reader nacionality', max_length=50)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Prestamo(models.Model):
    reader = models.ForeignKey(Lector, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
    )
    loan_date = models.DateField(auto_now=False, auto_now_add=False)
    return_date = models.DateField(
        blank=True,
        null=True
    )
    returned = models.BooleanField()

    objects = PrestamoManager()

    def __str__(self):
        return f'{self.id} - {self.book.title}'

