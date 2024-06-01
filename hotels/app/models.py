from django.db import models

# Create your models here.
class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)


class Pais(models.Model):
    countrycode = models.CharField(primary_key=True)
    countryname = models.CharField(max_length=50)


class Ciudad(models.Model):
    countrycode = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    citycode = models.CharField(primary_key=True)
    cityname = models.CharField(max_length=50)


class Hotel_info(models.Model):
    idhotel = models.AutoField(primary_key=True)
    citycode = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    hotelcode = models.CharField(max_length=100)
    hotelname = models.CharField(max_length=100)
    hotelrating = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    attractions = models.TextField(null=True)
    faxnumber = models.CharField(max_length=100, null=True)
    hotelfacilities = models.TextField(null=True)
    map = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=100, null=True)
    hotelwebsiteurl = models.CharField(max_length=200, null=True)

class Viaje(models.Model):
    idviaje = models.CharField(primary_key=True)
    idusuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    hotelcode = models.ForeignKey(Hotel_info, on_delete=models.SET_NULL, null=True)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    

    