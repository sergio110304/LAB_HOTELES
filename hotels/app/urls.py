from django.urls import path
from app.views import bienvenido, registrar, login, cuenta, editar, user_log, logout, agregar_vuelo, editar_vuelo, eliminar_vuelo, \
    escribir_reseña,homepage, catalogo, detalleshotel, get_ciudades
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', homepage, name='homepage'),
    # path('', bienvenido, name='index'),
    path('index', bienvenido, name='index'),
    path('registrar', registrar, name='registrar'),
    path('login', login, name='login'),
    path('cuenta/<int:idusuario>', cuenta, name='cuenta'),
    path('editar/<int:idusuario>', editar, name='editar'),
    path('user_log/<int:idusuario>/', user_log, name='user_log'),
    path('logout/', logout, name='logout'),
    path('agregar_vuelo', agregar_vuelo, name='agregar_vuelo'),
    path('editar_vuelo/<int:idvuelo>/', editar_vuelo, name='editar_vuelo'),
    path('eliminar_vuelo/<int:idvuelo>/', eliminar_vuelo, name='eliminar_vuelo'),
    path('escribir_reseña', escribir_reseña, name='escribir_reseña'),
    path('catalogo', catalogo, name='catalogo'),
    path('detalleshotel/<int:idhotel>', detalleshotel, name='detalleshotel'),
    path('get_ciudades', get_ciudades, name='get_ciudades'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)