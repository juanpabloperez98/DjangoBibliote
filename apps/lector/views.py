from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import PrestamoForm,MultiplePrestamoForm
from .models import Prestamo

# Create your views here.

class RegistrarPrestamo(FormView):
    template_name = "lector/add_prestamo.html"
    form_class = PrestamoForm
    success_url = "."


    def form_valid(self, form):

        # Prestamo.objects.create(
        #     reader = form.cleaned_data["reader"],
        #     book = form.cleaned_data["book"],
        #     loan_date = date.today(),
        #     returned = False
        # )

        prestamo = Prestamo(
            reader = form.cleaned_data["reader"],
            book = form.cleaned_data["book"],
            loan_date = date.today(),
            returned = False
        )

        prestamo.save()

        libro = form.cleaned_data["book"]
        libro.stoke -= 1
        libro.save()

        return super(RegistrarPrestamo, self).form_valid(form)



class AddPrestamo(FormView):
    template_name = "lector/add_prestamo.html"
    form_class = PrestamoForm
    success_url = "."


    def form_valid(self, form):
        
        obj, created = Prestamo.objects.get_or_create(
            reader=form.cleaned_data["reader"],
            book = form.cleaned_data["book"],
            returned = False,
            defaults={
                "loan_date":date.today()
            }
        )

        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect("/")


class AddMultiplePrestamo(FormView):
    template_name = "lector/add_multiple_prestamo.html"
    form_class = MultiplePrestamoForm
    success_url = "."


    def form_valid(self, form):
        print(form.cleaned_data["reader"])
        print(form.cleaned_data["books"])
        # 
        prestamos = []
        for b in form.cleaned_data["books"]:
            prestamo = Prestamo(
                reader = form.cleaned_data["reader"],
                book = b,
                loan_date = date.today(),
                returned = False
            )
            prestamos.append(prestamo)

        Prestamo.objects.bulk_create(
            prestamos
        )
        return super(AddMultiplePrestamo, self).form_valid(form)

