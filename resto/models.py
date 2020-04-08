from django.db import models
from django.conf import settings
from django.db.models import Avg
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen = models.ImageField(blank=True, null=True, upload_to='covers/%Y/%m/%D/')
    def __str__(self):
        return self.nombre

    @property
    def nombre_resto(self):
        padre = self.resto_nombre.all()
        return padre[0]
    
    @property
    def id_resto(self):
        padre = self.resto_nombre.all()
        return padre[0].id
    
    @property
    def average(self):
        plato_rating = self.plato.all().aggregate(Avg('calificacion')).get('calificacion__avg', 0.00)
        if plato_rating is None:
            plato_rating = 0.00
        return plato_rating

class Restaurante(models.Model):
    nombre = models.CharField(max_length=200)
    platos = models.ManyToManyField(Plato, blank=True, related_name='resto_nombre')
    descripcion = models.TextField()
    direccion = models.CharField(max_length=400)
    apertura = models.TimeField(null=True)
    cierre = models.TimeField(null=True)
    telefono = models.CharField(max_length=200, null=True)
    imagen_principal = models.ImageField(blank=True, null=True, upload_to='covers/%Y/%m/%D/')
    def __str__(self):
        return self.nombre

    @property
    def average_rating(self):
        restaurante_rating =  self.resto.all().aggregate(Avg('calificacion')).get('calificacion__avg', 0.0)
        if restaurante_rating is None:
            restaurante_rating = 0.0
        return restaurante_rating

class Imagen(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    imagen = models.FileField(blank=True, null=True, upload_to='covers/%Y/%m/%D/')

class ReviewPlato(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE, related_name='plato')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    calificacion = models.IntegerField(default=1)
    def __str__(self):
        return self.texto

class ReviewRestaurante(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='resto')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    calificacion = models.IntegerField(default=1)
    def __str__(self):
        return self.texto