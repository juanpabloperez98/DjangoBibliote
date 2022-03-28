from django.db import models
from django.db.models.signals import post_delete

from apps.autor.models import Persona
from apps.libro.models import Libro

from .managers import PrestamoManager


# Create your models here.
class Lector(Persona):
    
    class Meta:
        verbose_name = "Lector"
        verbose_name_plural = "Lectores"


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

    def save(self,*args, **kwargs):
        self.book.stoke -= 1
        self.book.save()
        super(Prestamo,self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.book.title}'

def update_libro_stok(sender, instance, **kwargs):
    instance.book.stoke += 1
    instance.book.save()

post_delete.connect(update_libro_stok, sender=Prestamo)