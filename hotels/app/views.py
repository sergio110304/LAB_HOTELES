from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.http import HttpResponse
from app.models import Usuario, Vuelo, Reseña, Hotel_info, Ciudad, Pais
from app.forms import UsuarioForm, VueloForm, ReseñaForm

# Create your views here.


def homepage(request):
    hoteles = Hotel_info.objects.distinct().filter(citycode='110718', hotelrating='All').values_list('hotelname', flat=True)[:3]
    context = {"hotel": hoteles}
    return render(request, 'homepage.html', context)

def catalogo(request):
    if request.method == 'POST':
        pais_ = request.POST.get('pais')
        ciudad_ = request.POST.get('ciudad')
        rating_ = request.POST.get('rating')

        # Comienza con todos los hoteles
        hoteles_filtrados = Hotel_info.objects.all()

        # Filtra por país si se seleccionó uno
        if pais_:
            ciudades_en_pais = Ciudad.objects.filter(countrycode=pais_)
            hoteles_filtrados = hoteles_filtrados.filter(citycode__in=ciudades_en_pais)

        # Filtra por ciudad si se seleccionó una
        if ciudad_:
            hoteles_filtrados = hoteles_filtrados.filter(citycode=ciudad_)

        # Filtra por rating si se seleccionó uno
        if rating_:
            hoteles_filtrados = hoteles_filtrados.filter(hotelrating=rating_)

        context = {
            "hoteles": hoteles_filtrados[:4],
            "hotelesfila2": hoteles_filtrados[4:8],
            "hotelesfila3": hoteles_filtrados[8:12],
            "paises": Pais.objects.all(),
            "ciudades": Ciudad.objects.all(),
            "ratings": Hotel_info.objects.values_list('hotelrating', flat=True).distinct(),
        }
        return render(request, 'catalogo.html', context)
    
    # Si no es un POST, muestra todos los hoteles
    context = {
        "hoteles": Hotel_info.objects.all()[:4],
        "hotelesfila2": Hotel_info.objects.all()[4:8],
        "hotelesfila3": Hotel_info.objects.all()[8:12],
        "paises": Pais.objects.all(),
        "ciudades": Ciudad.objects.all(),
        "ratings": Hotel_info.objects.values_list('hotelrating', flat=True).distinct(),
    }
    return render(request, 'catalogo.html', context)

def get_ciudades(request):
    countrycode = request.GET.get('countrycode')
    ciudades = Ciudad.objects.filter(countrycode=countrycode).values('citycode', 'cityname')
    return JsonResponse(list(ciudades), safe=False)

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
    return redirect('homepage')

def agregar_vuelo(request):
    if request.method == "POST":
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_vuelo')  # Redirigir a la misma página para mostrar la lista actualizada
    else:
        form = VueloForm()

    vuelos = Vuelo.objects.all()  # Obtener todos los vuelos

    return render(request, 'agregar_vuelo.html', {'form_vuelo': form, 'vuelos': vuelos})

def editar_vuelo(request, idvuelo):
    vuelo = get_object_or_404(Vuelo, idvuelo=idvuelo)
    if request.method == "POST":
        form = VueloForm(request.POST, instance=vuelo)
        if form.is_valid():
            form.save()
            return redirect('agregar_vuelo')
    else:
        form = VueloForm(instance=vuelo)
    
    return render(request, 'editar_vuelo.html', {'form_vuelo': form, 'vuelo': vuelo})

def eliminar_vuelo(request, idvuelo):
    vuelo = get_object_or_404(Vuelo, idvuelo=idvuelo)
    if request.method == "POST":
        vuelo.delete()
        return redirect('agregar_vuelo')
    
    return render(request, 'eliminar_vuelo.html', {'vuelo': vuelo})

def escribir_reseña(request):
    if request.method == 'POST':
        form_reseña = ReseñaForm(request.POST)
        if form_reseña.is_valid():
            form_reseña.save()
            return redirect('escribir_reseña')
    else:
        form_reseña = ReseñaForm()

    reseñas = Reseña.objects.all()

    return render(request, 'escribir_reseña.html', {'form_reseña': form_reseña, 'reseñas': reseñas})

def detalleshotel(request, idhotel):
    hotel = get_object_or_404(Hotel_info, pk=idhotel)
    return render(request, 'detalleshotel.html', {'hotel': hotel})