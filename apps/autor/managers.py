from django.db import models

from django.db.models import Q

class AutorManager(models.Manager):


    def buscar_autor(self, kword):
        resultado = self.filter(
            name__icontains=kword
        )
        return resultado

    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(name__icontains=kword) | Q(last_name__icontains=kword)
        )
        return resultado

    def buscar_autor3(self, kword):
        resultado = self.filter(
            name__icontains=kword
        ).exclude(edad=27)
        return resultado

    def buscar_autor4(self, kword):
        resultado = self.filter(
            name__icontains=kword
        ).exclude(
            Q(edad__icontains = 26) | Q(edad__icontains = 21)
        )
        return resultado

    def buscar_autor5(self, kword):
        resultado = self.filter(
            name__icontains=kword
        ).filter(
            Q(edad__icontains = 26) | Q(edad__icontains = 21)
        )
        return resultado

    def buscar_autor6(self, kword):
        resultado = self.filter(
            edad__gt=22,
            edad__lt=65
        ).order_by('last_name','name')
        return resultado
    