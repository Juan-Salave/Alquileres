from django.shortcuts import render
from .models import Departamento
from django.views.generic.detail import DetailView

def home(request):
    departamentos = Departamento.objects.all()
    data = {
        'departamentos':departamentos
    }
    return render(request, 'departamentos/home.html', data)

class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'departamentos/departamento.html'
