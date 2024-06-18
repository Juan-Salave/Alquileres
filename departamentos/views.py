from django.shortcuts import render
from .models import Departamento, Location
from django.views.generic.detail import DetailView
import folium


def home(request):

    departamentos = Departamento.objects.all()

    locations     = Location.objects.all()
    initialMap    = folium.Map(location=[-34.594375,-58.4458285], zoom_start = 12) 

    for location in locations:
        coordinates = (location.lat, location.lng)
        folium.Marker(coordinates, location.direccion).add_to(initialMap)
        
        
    data = {
        'map':initialMap._repr_html_(),
        'departamentos':departamentos
        }         
    return render(request, 'departamentos/home.html', data)

class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'departamentos/departamento.html'
