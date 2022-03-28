from django.contrib import admin
from django.urls import path,include


from . import views


urlpatterns = [
    path('prestamos/add/', views.AddPrestamo.as_view(), name='prestamos-add'),
    path('prestamos/multiple/add/', views.AddMultiplePrestamo.as_view(), name='prestamos-multiple-add'),
]
