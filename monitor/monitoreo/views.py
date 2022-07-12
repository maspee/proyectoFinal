from django.shortcuts import render, redirect
from django .http import HttpResponse
from .models import Receta
from .forms import RecetaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def recetas(request): 
    recetas = Receta.objects.all()
    return render(request, 'crud/index.html', {'recetas': recetas})

def crear(request):
    formulario = RecetaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.instance.autor = request.user
        formulario.save()
        return redirect('recetas')
    return render(request, 'crud/crear.html', {'formulario': formulario})

def editar(request, id): 
    receta = Receta.objects.get(id=id)
    if request.user == receta.autor:
        formulario = RecetaForm(request.POST or None, request.FILES or None, instance=receta)
        if formulario.is_valid() and request.POST:
            formulario.save()
            return redirect('recetas')
        return render(request, 'crud/editar.html', {'formulario': formulario})
    return redirect('recetas')

def eliminar(request, id):
    receta = Receta.objects.get(id=id)
    if request.user == receta.autor:
        receta.delete()
        return redirect('recetas')
    return redirect('recetas')

def envio_mail(request):
    send_mail('Asunto de correo',
    'Contenido del correo.',
    'recetamonitor@gmail.com',
    [request.user.email],
    fail_silently=False,) 
    return HttpResponse('<h1>Correo enviado</h1>')
