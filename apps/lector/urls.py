from django.contrib import admin
from django.urls import path,include


from . import views


urlpatterns = [
    path('prestamos/add/', views.RegistrarPrestamo.as_view(), name='prestamos-add'),
]
