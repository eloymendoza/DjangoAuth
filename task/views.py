from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Registrar usuario
                usuario = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                return HttpResponse('Usuario creado con exito')
            except:
                return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

