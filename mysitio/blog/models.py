from django.db import models
from django.utils import timezone
# Create your models here.
#define nuestro modelo (objeto) dentro tendra sus propiedades con sus definiciones
#class me dice que estoy creando un objeto. Post es el nombre del modelo
class Post(models.Model): 
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)#models.CharField define un texto con numero limitado de caracteres
    text = models.TextField()#models.TextField textos largos sin limite (contenido posteo)
    created_date = models.DateTimeField(default=timezone.now)#fecha y hora
    published_date = models.DateTimeField(blank=True, null=True)
#models.Model significa que Post es un modelo de django asique
# debe guardarlo en una Base de Datos    

    def publicar(self):#es el metodo para publicar en el blog def(funcion)
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#cuando lo llamemos, va a devolver el titulo del post.
        return self.title
