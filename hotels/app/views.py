from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.http import HttpResponse
from app.models import Usuario
from app.forms import UsuarioForm

# Create your views here.

def bienvenido(request):
    no_usuarios = Usuario.objects.count()
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {'no_usuarios': no_usuarios, 'usuarios': usuarios})

def registrar(request):
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST)
        if form_usuario.is_valid():
            username = form_usuario.cleaned_data.get('username')
            if Usuario.objects.filter(username=username).exists():
                return render(request, 'registrar.html', {'form_usuario': form_usuario, 'error': 'El nombre de usuario ya existe'})
            else:
                form_usuario.save()
                return redirect('index')
    else:
        form_usuario = UsuarioForm()

    return render(request, 'registrar.html', {'form_usuario': form_usuario})


def login(request):
    if request.method == 'POST':
        username_ = request.POST['username']
        password_ = request.POST['password']
        try:
            user = Usuario.objects.get(username=username_)
            if user.password == password_:
                return redirect('cuenta', idusuario=user.idusuario)
            else:
                return render(request, 'login.html', {'error': 'Contraseña incorrecta'})
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'error': 'El usuario no existe'})
    else:
        return render(request, 'login.html')
    
def cuenta(request, idusuario):
    usuario = Usuario.objects.get(pk=idusuario)
    return render(request, 'cuenta.html', {'usuario': usuario})