from django.contrib import admin
from .models import Contacto , Perfil

# Register your models here.
admin.site.register(Contacto)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')