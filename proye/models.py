from django.db import models

# Create your models here.
class Material(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    material = models.CharField(max_length=20)
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
    def __str__(self):
        return self.material

class Marca(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    marca = models.CharField(max_length=20)
    imagenmarca= models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    grupo= models.IntegerField(default=1)
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
    def __str__(self):
        return self.marca

class Edad(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    edad = models.CharField(max_length=20)
    rangoedad = models.CharField(max_length=20)
    class Meta:
        verbose_name = "Edad"
        verbose_name_plural = "Edades"
    def __str__(self):
        return self.rangoedad

class Categoria(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    catego = models.CharField(max_length=20)
    rangoedad =  models.ForeignKey(Edad,on_delete=models.CASCADE,verbose_name="Rango de edad")
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    def __str__(self):
        return self.catego

class Productos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    marca=models.ForeignKey(Marca,on_delete=models.CASCADE,verbose_name="Marca")
    material=models.ForeignKey(Material,on_delete=models.CASCADE,verbose_name="Material")
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,verbose_name="Categoria")
    rangoedad =  models.ForeignKey(Edad,on_delete=models.CASCADE,verbose_name="Rango de edad",default=1)
    nombre = models.TextField()
    descripcion= models.TextField()
    destacado = models.BooleanField()
    grupo= models.IntegerField(default=1)
    imagen= models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    def __str__(self):
        return self.nombre
        