from django.db import models
from proye.models import Productos
class Usuario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.TextField()
    password= models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    imagenesdeperfil= models.ImageField(null=True,upload_to="usuarios",verbose_name="Fotografía")
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario=models.CharField(max_length=10 ,null=True)
    comentario = models.TextField()
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado",null=True)
    producto =  models.ForeignKey(Productos,on_delete=models.CASCADE,verbose_name="Productos",default=1)
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
    def __str__(self):
        return self.comentario

class Coment(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario=models.CharField(max_length=10)
    comentario = models.TextField()
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado",null=True)
    class Meta:
        verbose_name = "Coment"
        verbose_name_plural = "Coments"
    def __str__(self):
        return self.comentario
class User(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre = models.TextField()
    apellido = models.TextField()
    correo = models.TextField()
    password= models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Useres"
    def __str__(self):
        return self.nombre