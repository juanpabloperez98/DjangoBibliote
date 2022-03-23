import datetime

from django.db import models
from django.db.models import Q, Count, Avg
from django.db.models.functions import Lower

class PrestamoManager(models.Manager):

    def libros_promedio_edades(self):
        resultado = self.filter(
            book__id = '6'
        ).aggregate(
            prom_edad = Avg('reader__edad')
        )
        return resultado

    def libros_promedio_annotate(self):
        resultado = self.filter(
            book__id = '6' 
        ).annotate(
            prom_edad = Avg('reader__edad')
        )

        for r in resultado:
            print("**************")
            print(r,r.prom_edad)

        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            'book'
        ).annotate(
            num_prestados=Count('book'),
            title = Lower('book__title')
        )

        for r in resultado:
            print("******")
            print(r, r['num_prestados'])

        return resultado


