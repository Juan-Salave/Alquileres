from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    
    path("departamento/<pk>", views.DepartamentoDetailView.as_view(), name="Departamento"),
]