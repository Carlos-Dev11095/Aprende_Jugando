from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from usuarios.models import Perfil,Contacto
from comentarios.models import Comentario
class ContactoForm(forms.ModelForm):
    class Meta:
      model = Contacto
      fields = ['Nombre','Telefono','Mensaje']

class ComentForm(forms.ModelForm):
    class Meta:
      model = Comentario
      fields = ['usuario','comentario','producto']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
