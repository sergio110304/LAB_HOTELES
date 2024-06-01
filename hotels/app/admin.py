from django.contrib import admin
from app.models import Usuario, Pais, Ciudad, Hotel_info, Viaje

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Hotel_info)
admin.site.register(Viaje)
