from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Publicacion
from .forms import PublicacionForm

def publicacion(request):
    posts = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/contacto.html', {'posts': posts})
   
def publicacion_detalle(request, pk):
    post = get_object_or_404(Publicacion,pk=pk)
    return render(request,'blog/publicacion_detalle.html', {'post': post})

def publicacion_nueva(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('publicacion_detalle', pk=post.pk)
    else:
        form = PublicacionForm()
    return render(request, 'blog/publicacion_editar.html', {'form': form})

def publicacion_editar(request, pk):
    post = get_object_or_404(Publicacion,pk=pk)
    if request.user == post.autor:
        if request.method == "POST":
            form = PublicacionForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.fecha_publicacion = timezone.now()
                post.save()
                return redirect('publicacion_detalle', pk=post.pk)
        else:
            form = PublicacionForm(instance=post)
        return render(request, 'blog/publicacion_editar.html', {'form': form})
    return redirect('publicacion')

def publicacion_eliminar(request, pk):
    post = Publicacion.objects.get(pk=pk)
    if request.user == post.autor:
        post.delete()
        return redirect('publicacion')
    return redirect('publicacion')

    
    