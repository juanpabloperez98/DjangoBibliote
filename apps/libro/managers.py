import datetime

from django.contrib.postgres.search import TrigramSimilarity
from django.db import models
from django.db.models import Count, Q

from apps import libro


class LibroManager(models.Manager):


    def listar_libros(self, kword):
        resultado = self.filter(
            title__icontains=kword,
            date__range=('2000-01-01','2010-01-01')
        )
        return resultado


    def listar_libros_trg(self, kword):
        if kword:
            resultado = self.filter(
                title__trigram_similar=kword,
            )
        else: resultado = self.all()[:10]
        return resultado

    def listar_libros2(self, kword, fecha1, fecha2):
        date1 = datetime.datetime.strptime(fecha1,'%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha2,'%Y-%m-%d').date()
        resultado = self.filter(
            title__icontains=kword,
            date__range=(date1,date2)
        )
        return resultado
    
    def listar_libros_categoria(self, categoria):
        return self.filter(
            category__id = categoria
        ).order_by('title')

    def add_autor_libro(self,libro_id,autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro
    
    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamo = Count('libro_prestamo')
        )
        return resultado

    def num_libros_prestamos(self):
        resultado = self.annotate(
            num_prestados=Count('libro_prestamo')
        ) 

        for r in resultado:
            print("******")
            print(r, r.num_prestados)

        return resultado 

class CategoryManager(models.Manager):
    def category_por_autor(self,autor):
        return self.filter(
            category_libro__autores__id = autor
        ).distinct()

    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros = Count('category_libro')
        )

        for r in resultado:
            print('*********')
            print(r, r.num_libros)

        return resultado
    
        
        
