from django.contrib import admin
from .models import Libro,Categoria

# Register your models here.

class LibroModel(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "date",
    )
    search_fields = ("title",)
    list_filter = ("date",)

class CategoryModel(admin.ModelAdmin):
    
    search_fields = ("name",)

admin.site.register(Categoria,CategoryModel)
admin.site.register(Libro,LibroModel)