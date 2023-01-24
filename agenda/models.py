from django.db import models

# Create your models here.

class contacto(models.Model):
	nombre = models.CharField(max_length=500)
	email = models.CharField(max_length=500)
	phone = models.CharField(max_length=500)
