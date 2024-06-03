from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from app.models import Usuario, Vuelo, Reseña
from app.forms import UsuarioForm, VueloForm, ReseñaForm

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

def editar(request, idusuario):
    usuario = get_object_or_404(Usuario, pk=idusuario)
    if request.method == 'POST':
        form_usuario = UsuarioForm(request.POST, instance=usuario)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('cuenta', idusuario=idusuario)
    else:
        form_usuario = UsuarioForm(instance=usuario)

    return render(request, 'editar.html', {'form_usuario': form_usuario})


def login(request):
    if request.method == 'POST':
        username_ = request.POST['username']
        password_ = request.POST['password']
        try:
            user = Usuario.objects.get(username=username_)
            if user.password == password_:
                return redirect('user_log', idusuario=user.idusuario)
            else:
                return render(request, 'login.html', {'error': 'Contraseña incorrecta'})
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'error': 'El usuario no existe'})
    else:
        return render(request, 'login.html')

def user_log(request, idusuario):
    usuario = get_object_or_404(Usuario, pk=idusuario)
    if request.method == "POST" and "ver_cuenta" in request.POST:
        return redirect('cuenta', idusuario=idusuario)
    return render(request, 'index2.html', {'usuario': usuario})

def cuenta(request, idusuario):
    usuario = get_object_or_404(Usuario, pk=idusuario)
    return render(request, 'cuenta.html', {'usuario': usuario})

def logout(request):
    auth_logout(request)
    return redirect('index')

def agregar_vuelo(request):
    if request.method == 'POST':
        form_vuelo = VueloForm(request.POST)
        if form_vuelo.is_valid():
            form_vuelo.save()
            return redirect('index')
    else:
        form_vuelo = VueloForm()
    return render(request, 'agregar_vuelo.html', {'form_vuelo': form_vuelo})

def escribir_reseña(request):
    if request.method == 'POST':
        form_reseña = ReseñaForm(request.POST)
        if form_reseña.is_valid():
            form_reseña.save()
            return redirect('index')
    else:
        form_reseña = ReseñaForm()
    return render(request, 'escribir_reseña.html', {'form_reseña': form_reseña})