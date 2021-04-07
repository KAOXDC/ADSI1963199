from django import forms
from django.contrib.auth.models import User
from .models import *

class agregar_producto_form (forms.ModelForm):
    class Meta:
        model = Producto
        fields= '__all__'
        #fields= ['nombre', 'precio', 'marca']
        #exclude= ['nombre', 'precio', 'marca']

class user_form (forms.ModelForm):
    password = forms.CharField(label='Clave', widget=forms.PasswordInput(render_value = False))
    class Meta:
        model = User 
        fields = ['username', 'email', 'password', ]


class registrarse_form (forms.ModelForm):
    class Meta:
        model = Persona 
        fields = '__all__'
        exclude = ['user']
