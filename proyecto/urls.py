"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from proye import views  as views_proyecto
from django.conf import settings 
from proye.views import SignUpView ,SignOutView, BienvenidaView,SignInView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_proyecto.proyecto, name="Principal"),
    path('producto/<int:id>',views_proyecto.producto, name="Producto"),
    path('filtrado/<marca>',views_proyecto.filtrado, name="Filtros"),
    path('filtradoe/<rangoedad>',views_proyecto.filtrado2, name="Filtrose"),
    path('filtradoc/<categoria>',views_proyecto.filtrado3, name="Filtrosc"),
    path('contacto/',views_proyecto.contacto, name="Contacto"),
    path('contactoreg/',views_proyecto.regcon, name="RegCon"),
    path('comreg/<int:id>',views_proyecto.regcom, name="RegCom"),
    
    # path('', BienvenidaView.as_view(), name='bienvenida'),
     path('registrate/', SignUpView.as_view(), name='sign_up'),
     path('incia-sesion/', SignInView.as_view(), name='sign_in'),
     path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
