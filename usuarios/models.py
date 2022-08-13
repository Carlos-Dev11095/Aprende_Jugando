from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Contacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    Nombre = models.TextField()
    Telefono = models.TextField()
    Mensaje = models.TextField()
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
class Perfil(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=255,blank=True)
    web = models.URLField(blank=True)

    def __str__(self) :
        return self.usuario.username()
@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()

    
