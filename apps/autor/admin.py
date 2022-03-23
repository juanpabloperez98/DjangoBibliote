from django.contrib import admin
from .models import Autor

# Register your models here.

class AutorModel(admin.ModelAdmin):
    list_display = (
        "name",
        "last_name",
        "nationality"
    )
    search_fields = ("name",)
    list_filter = ("edad",)

admin.site.register(Autor,AutorModel)