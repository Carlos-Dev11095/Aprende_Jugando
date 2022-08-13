from dataclasses import fields
from django import forms
from .models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nombre','apellido','correo','password']

