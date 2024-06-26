from django.db import models

class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre

class Moneda (models.Model):
    moneda = models.CharField(max_length=30)
    
    def __str__(self):
        return self.moneda
    
class Departamento(models.Model):
    titulo1       = models.CharField(max_length=50)
    titulo2       = models.CharField(max_length=50)
    direccion     = models.CharField(max_length=50)
    descripcion1  = models.TextField(null=True)
    descripcion2  = models.TextField(null=True)
    precio        = models.IntegerField()
    habitaciones  = models.IntegerField()
    banios        = models.IntegerField()
    huespedes     = models.IntegerField()
    area          = models.IntegerField()
    clave         = models.CharField(max_length=20, null=True)
    barrio        = models.ForeignKey(Barrio, on_delete=models.PROTECT)
    moneda        = models.ForeignKey(Moneda, on_delete=models.PROTECT, null=True )
       
    def __str__(self):
        return self.titulo1    
class ImagenDepartamentos(models.Model):
    imagen        = models.ImageField(upload_to="producto")
    departamento  = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name="imagenes")  
    
class Location(models.Model):
    name        = models.CharField(max_length=50)
    direccion   = models.CharField(max_length=50)
    lat         = models.FloatField(verbose_name='Latitud')
    lng         = models.FloatField(verbose_name='Longitud')
    class Meta:

        verbose_name_plural ='Ubicacion'
        ordering            = ['direccion']
           
    def __str__(self):
        return self.name 
     
    
# falta colocar y aptualizar el admin