from django.shortcuts import render
from .models import Departamento
from django.views.generic.detail import DetailView
import folium

# def home(request):
#     departamentos = Departamento.objects.all()
#     data = {
#         'departamentos':departamentos
#     }
#     return render(request, 'departamentos/home.html', data)

def home(request):
    # get departamentos
    departamentos = Departamento.objects.all()
    # Get ubicacion
    initialMap = folium.Map(location=[-34.594375,-58.4458285], zoom_start = 12) 
    # Context con multiples parametros
    data = {
        'map':initialMap._repr_html_(),
        'departamentos':departamentos
        }         
    return render(request, 'departamentos/home.html', data)

class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'departamentos/departamento.html'
