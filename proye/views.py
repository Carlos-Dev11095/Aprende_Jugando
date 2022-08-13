from django.shortcuts import render , redirect
from .models import Categoria, Edad, Marca
from .models import Productos
from comentarios.models import Usuario,Comentario
from comentarios.forms import UserForm
from django.contrib.auth import login, authenticate

from django.views.generic import CreateView, TemplateView

from usuarios.models import Perfil

from .forms import SignUpForm,ContactoForm,ComentForm
from django.contrib.auth.views import LoginView, LogoutView 

class SignOutView(LogoutView):
    pass
class SignInView(LoginView):
    template_name = 'proye/inicioreg.html'
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'proye/index.html'
def proyecto(request):
    productodes=Productos.objects.filter(destacado=True)
    productoj=Productos.objects.filter(categoria=2)
    todos=Productos.objects.all()
    marcas=Marca.objects.all()
    marcaid=Marca.objects.filter(grupo = 1)
    marcaid2=Marca.objects.filter(grupo = 2)
    marcaid3=Marca.objects.filter(grupo = 3)
    marcasd=Marca.objects.get(id=1)
    marcasd2=Marca.objects.get(id=2)
    marcasd8=Marca.objects.get(id=8)
    edades=Edad.objects.all()
    catego=Categoria.objects.all()    
    return render(request,"proye/index.html",{'todos':todos,'productodes':productodes 
    ,'productoj':productoj,'marcas':marcas ,'marcaid':marcaid ,'marcaid2':marcaid2,'marcaid3':marcaid3,'edades':edades,'catego':catego,'marcasd':marcasd,'marcasd2':marcasd2,'marcasd8':marcasd8})

def producto(request,id):
    producto=Productos.objects.get(id=id)
    productodes=Productos.objects.filter(destacado=True)
    marcas=Marca.objects.all()
    edades=Edad.objects.all()
    catego=Categoria.objects.all()
    usuario=Usuario.objects.all()
    coment=Comentario.objects.filter(producto=producto.id)
    return render(request,"proye/producto.html",{'producto':producto,'marcas':marcas,'edades':edades,'catego':catego,'productodes':productodes,'usuario':usuario,'coment':coment})

def filtrado(request,marca):
    producto=Productos.objects.filter(marca=marca)
    
    marcas=Marca.objects.all()
    edades=Edad.objects.all()
    catego=Categoria.objects.all()
    return render(request,"proye/filtrado.html",{'marcas':marcas,'producto':producto,'edades':edades,'catego':catego})

def contacto(request):
    return render(request,"proye/contacto.html")

def secion(request):
    return render(request,"proye/inicioreg.html")

def reg(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'proye/index.html')
    form = UserForm()
#Si algo sale mal se reenvian al f
    return render(request,"proye/inciosesion.html",{'form': form})

def filtrado2(request,rangoedad):
    
    producto=Productos.objects.filter(rangoedad=rangoedad)
    
    marcas=Marca.objects.all()
    edades=Edad.objects.all()
    catego=Categoria.objects.all()
    return render(request,"proye/filtrado.html",{'marcas':marcas,'producto':producto,'edades':edades,'catego':catego})

def filtrado3(request,categoria):
    
    producto=Productos.objects.filter(categoria=categoria)
    marcas=Marca.objects.all()
    edades=Edad.objects.all()
    catego=Categoria.objects.all()
    return render(request,"proye/filtrado.html",{'marcas':marcas,'producto':producto,'edades':edades,'catego':catego})

def regcon(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'proye/contacto.html')
    form = ContactoForm()
#Si algo sale mal se reenvian al f
    return render(request,"proye/contacto.html",{'form': form})

def regcom(request,id):
    producto=Productos.objects.get(id=id)
    productodes=Productos.objects.filter(destacado=True)
    marcas=Marca.objects.all()
    edades=Edad.objects.all()
    catego=Categoria.objects.all()
    usuario=Usuario.objects.all()
    coment=Comentario.objects.filter(producto=producto.id)
    if request.method == 'POST':
        form = ComentForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'proye/producto.html',{'form': form,'producto':producto,'marcas':marcas,'edades':edades,'catego':catego,'productodes':productodes,'usuario':usuario,'coment':coment})
    form = ComentForm()
#Si algo sale mal se reenvian al f
    return render(request,"proye/index.html",{'form': form})