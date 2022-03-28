from datetime import date

from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import PrestamoForm
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
