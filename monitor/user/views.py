from urllib import request
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            print(usuario)
    form = UserRegistrationForm()
    return render(request, 'user/registro.html', {'form': form}) 

@login_required
def perfil(request):
    return render(request, 'user/perfil.html')