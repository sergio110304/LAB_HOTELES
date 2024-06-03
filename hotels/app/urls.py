from django.urls import path
from app.views import bienvenido, registrar, login, cuenta, editar, user_log, logout, agregar_vuelo, escribir_reseña
urlpatterns = [
    path('', bienvenido, name='index'),
    path('index', bienvenido, name='index'),
    path('registrar', registrar, name='registrar'),
    path('login', login, name='login'),
    path('cuenta/<int:idusuario>', cuenta, name='cuenta'),
    path('editar/<int:idusuario>', editar, name='editar'),
    path('user_log/<int:idusuario>/', user_log, name='user_log'),
    path('logout/', logout, name='logout'),
    path('agregar_vuelo', agregar_vuelo, name='agregar_vuelo'),
    path('escribir_reseña', escribir_reseña, name='escribir_reseña'),
]