from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def signup(request):
    if request.method == 'GET':
        print('Enviando formulario')
    else:
        print(request.POST)
        print('Obteniendo datos')
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })
