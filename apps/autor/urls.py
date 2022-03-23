from django.contrib import admin
from django.urls import path,include


from . import views


urlpatterns = [
    path('autores/', views.AutoresListView.as_view(), name='autores'),
]
