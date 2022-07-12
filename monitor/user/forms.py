from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label = 'Nombre de Usuario', required=True) 
    email = forms.EmailField(label= 'Email', required=True)
    password1 = forms.CharField(label = "Contraseña", required=True)
    password2 = forms.CharField(label = "Confirmar Contraseña", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

