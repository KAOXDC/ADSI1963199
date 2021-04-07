from django.shortcuts import render, redirect
from .models import Producto
from .forms import *
# Create your views here.
def index_view (request):
    return render(request, 'index.html', locals())

def about_view (request):
    return render(request, 'about.html', locals())

def listar_producto_view (request):
    lista = Producto.objects.filter() # SELECT * FROM Producto
    return render(request, 'listar_producto.html', locals())

def agregar_producto_view(request): 
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('/listar_producto/')
    else:
        formulario = agregar_producto_form()
    return render(request, 'agregar_producto.html', locals())

def ver_producto_view(request, id_prod):
    p = Producto.objects.get(id=id_prod)
    return render(request, 'ver_producto.html', locals())

def editar_producto_view(request, id_prod): 
    p = Producto.objects.get(id=id_prod)
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES, instance = p)
        if formulario.is_valid():
            p = formulario.save()
            return redirect ('/listar_producto/')
    else:
        formulario = agregar_producto_form(instance = p)
    return render(request, 'agregar_producto.html', locals())

def eliminar_producto_view(request, id_prod):
    p = Producto.objects.get(id=id_prod)
    p.delete()
    return redirect ('/listar_producto/')


def registrarse_view (request):

    usu = ""
    ema = ""
    cla = ""
    if request.method == 'POST':
        form_user = user_form(request.POST)
        form_persona = registrarse_form(request.POST, request.FILES)
        if form_persona.is_valid() and form_user.is_valid():
            usu = form_user.cleaned_data['username']  
            ema = form_user.cleaned_data['email'] 
            cla = form_user.cleaned_data['password']
            u = User.objects.create_user(username=usu, email=ema, password=cla)

            p = form_persona.save(commit = False)
            p.user = u 
            u.save()
            p.save()
    else: # cuando es metodo GET
        form_user = user_form()
        form_persona = registrarse_form()
    return render(request, 'registrarse.html', locals())