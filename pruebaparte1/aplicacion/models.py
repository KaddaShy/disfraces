from django.db import models

# Create your models here.


class Disfraces(models.Model):
    Nombre_disfraz = models.CharField(max_length=50, null=True)
    Talla = models.CharField(max_length=50,null=True)
    Para = models.CharField(max_length=50,null=True)
    Precio = models.IntegerField(null=True)
    Estado = models.IntegerField(null=True)
    Accesorios = models.CharField(max_length=100, null=True)




class Arrendatario(models.Model):
    ID = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    fono = models.IntegerField(null=True)
    descripcion = models.TextField(null=True)
    fecha_arriendo = models.DateField(null=True)
    fecha_entrega = models.DateField(null=True)
    codigo_disfraz = models.ForeignKey(Disfraces, on_delete=models.PROTECT, null=True)
