from django.db import models
from .managers import AutorManager

# Create your models here.
class Persona(models.Model):
    name = models.CharField('Autor name', max_length=50)
    last_name = models.CharField('Autor last name', max_length=50)
    nationality = models.CharField('Autor nationality', max_length=30)
    edad = models.PositiveIntegerField()


    objects = AutorManager()

    def __str__(self):
        return f'{self.id} - {self.name} - {self.last_name}'

    class Meta:
        abstract = True

class Autor(Persona):
    pseudonym = models.CharField("Pseudonym", max_length=50, blank=True)
    objects = AutorManager()