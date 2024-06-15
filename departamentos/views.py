from django.shortcuts import render
from .models import Departamento,Barrio

def home(request):
    departamentos = Departamento.objects.all()
    data = {
        'departamentos':departamentos
    }
    return render(request, 'departamentos/home.html', data)
