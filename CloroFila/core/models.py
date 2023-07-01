from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre



class producto(models.Model):
     nombre = models.CharField(max_length=50) 
     precio = models.IntegerField()
     descripcion = models.TextField()
     exterior = models.BooleanField()
     categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT) 
     fecha_germinacion = models.DateField()
     imagen = models.ImageField(null=True, blank=True)
     stock = models.IntegerField(default=0)
     
  
     def __str__(self):
        return self.nombre
     


