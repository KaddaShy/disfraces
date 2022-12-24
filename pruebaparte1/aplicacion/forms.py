from django import forms
from django.core import validators
from .models import Disfraces


class INGRESARDISFRAZ(forms.ModelForm):
    class Meta:
        model = Disfraces
        fields = ("Nombre_disfraz","Talla","Para","Precio","Estado","Accesorios")

class DisfrazForm(forms.ModelForm):
    ESTADOS = [('en arriendo', 'EN ARRIENDO'),
               ('atrasado', 'ATRASADO'), ('devuelto', 'DEVUELTO')]
    nombre_disfraz = forms.CharField(label='Nombre Disfraz', validators=[
        validators.MinLengthValidator(10),
        validators.MaxLengthValidator(20)])
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    nombre_disfraz.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'


class Eliminardisfraces(forms.Form):

    ESTADOS = [('en arriendo', 'EN ARRIENDO'),
               ('atrasado', 'ATRASADO'), ('devuelto', 'DEVUELTO')]
    nombre_disfraz = forms.CharField(label='Nombre Disfraz', validators=[
        validators.MinLengthValidator(10),
        validators.MaxLengthValidator(20)
    ])

    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    nombre_disfraz.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'


class Modificardisfraz(forms.Form):

    ESTADOS = [('en arriendo', 'EN ARRIENDO'),
               ('atrasado', 'ATRASADO'), ('devuelto', 'DEVUELTO')]
    nombre_disfraz = forms.CharField(label='Nombre Completo', validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(10)
    ])

    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    nombre_disfraz.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
