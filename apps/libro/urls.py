from django.contrib import admin
from django.urls import path,include


from . import views


urlpatterns = [
    path('libros/', views.LibrosListView.as_view(), name='libros'),
    path('libros-2/', views.LibrosList2View.as_view(), name='libros2'),
    path('libros-detalle/<pk>', views.LibroDetailView.as_view(), name='libros-detail'),
]
