from django.contrib import admin

from .models import User, Usuario
from .models import Comentario
# Register your models here.
class AdministrarUsuarios(admin.ModelAdmin):
 list_display =('id','nombre')
 search_fields =('id','nombre')
admin.site.register(User ,AdministrarUsuarios )

admin.site.register(Usuario)
admin.site.register(Comentario)
