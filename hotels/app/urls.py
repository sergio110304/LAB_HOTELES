from django.urls import path
from app.views import bienvenido, registrar, login, cuenta, editar
urlpatterns = [
    path('', bienvenido, name='index'),
    path('index', bienvenido, name='index'),
    path('registrar', registrar, name='registrar'),
    path('login', login, name='login'),
    path('cuenta/<int:idusuario>', cuenta, name='cuenta'),
    path('editar/<int:idusuario>', editar, name='editar'),
]