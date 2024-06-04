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

    def __str__(self):
        return f"Usuario {self.idusuario}: {self.nombre} {self.apellido} {self.telefono}"


class Pais(models.Model):
    countrycode = models.CharField(primary_key=True)
    countryname = models.CharField(max_length=50)

    def __str__(self):
        return f"País {self.countrycode}: {self.countryname}"


class Ciudad(models.Model):
    countrycode = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    citycode = models.CharField(primary_key=True)
    cityname = models.CharField(max_length=50)

    def __str__(self):
        return f"Ciudad {self.citycode}: {self.cityname}"


class Hotel_info(models.Model):
    idhotel = models.AutoField(primary_key=True)
    citycode = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    hotelcode = models.CharField(max_length=200)
    hotelname = models.CharField(max_length=200)
    hotelrating = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    attractions = models.TextField(null=True)
    faxnumber = models.CharField(max_length=200, null=True)
    hotelfacilities = models.TextField(null=True)
    map = models.CharField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=200, null=True)
    pincode = models.CharField(max_length=200, null=True)
    hotelwebsiteurl = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.idhotel} {self.hotelname} "

class Viaje(models.Model):
    idviaje = models.CharField(primary_key=True)
    idusuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    hotelcode = models.ForeignKey(Hotel_info, on_delete=models.SET_NULL, null=True)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    
class Vuelo(models.Model):
    idvuelo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()

    def __str__(self):
        return f"Viaje desde {self.origen} a {self.destino} de {self.fecha_salida} a {self.fecha_regreso}"

class Reseña(models.Model):
    idreseña = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    hotel = models.TextField()
    texto = models.TextField()
    puntuacion = models.IntegerField()

    def __str__(self):
        return f"Reseña {self.idreseña} por {self.usuario} para {self.hotel}"
    