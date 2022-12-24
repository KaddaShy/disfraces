from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import Disfraces
from . import forms
from .forms import INGRESARDISFRAZ, Eliminardisfraces
# Create your views here.

def visualizardisfraz(request):
    disfraces123 = Disfraces.objects.all()
    data = {'disfraces': disfraces123}
    return render(request, 'disfraces.html', data)

    
def display(request):
    return HttpResponse("<h1> Hola... aqui no hay nada...</h1>")


def inicio(request):
    return render(request, 'principalTienda.html')


def agregardisfraces(request):
    form = INGRESARDISFRAZ()
    if request.method == 'POST':
        form = INGRESARDISFRAZ(request.POST)
        if form.is_valid():
            form.save()

    data = {'form': form}
    return render(request, 'agregardisfraces.html', data)


def eliminardisfraces(request, id):
    disfraz = Disfraces.objects.get(id = id)
    disfraz.delete()
    return redirect('/disfraces')


def modificardisfraces(request, id):
    disfraz = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=disfraz)
    if request.method == 'POST' :
        form = FormProyecto(request.POST, instance=disfraz)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    form = forms.Modificardisfraz()
    if request.method == 'POST':
        form = forms.Modificardisfraz(request.POST)
        if forms.is_valid():
            print("Disfraz modificado")
            print("Nombre:", form.cleaned_data['nombre'])
            print("Estado", form.cleaned_data['estado'])

    data = {'form': form}
    return render(request, 'agregardisfraces.html', data)



