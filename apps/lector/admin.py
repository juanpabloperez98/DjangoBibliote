from django.contrib import admin

from .models import Prestamo,Lector
# Register your models here.

class ReaderModel(admin.ModelAdmin):
    list_display = (
        "name",
        "nationality",
        "edad",
    )
    search_fields = ("name",)
    list_filter = ("nationality",)

class PrestamoModel(admin.ModelAdmin):
    list_display = (
        "book",
        "loan_date",
        "return_date",
    )
    search_fields = ("book",)
    list_filter = ("loan_date",)


admin.site.register(Prestamo,PrestamoModel)
admin.site.register(Lector,ReaderModel)
