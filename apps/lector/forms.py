from django import forms

from apps.libro.models import Libro

from .models import Prestamo


class PrestamoForm(forms.ModelForm):


    class Meta:
        model = Prestamo
        fields = (
            "reader",
            "book"
        )


class MultiplePrestamoForm(forms.ModelForm):

    books = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Prestamo
        fields = (
            "reader",
        )
    
    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm,self).__init__(*args, **kwargs)
        self.fields["books"].queryset = Libro.objects.all()
