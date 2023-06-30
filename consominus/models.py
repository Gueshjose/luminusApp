from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Utilisateur(models.Model):
    name=models.CharField(max_length=20)
    numeroClient=models.CharField(max_length=15)
    image=models.ImageField(upload_to='images/')
    mail=models.EmailField()
    gsm=models.CharField(max_length=12)
    conseillé=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Luminus(models.Model):
    green=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    grey=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

class Contrat(models.Model):
    tarifHoraire=models.FloatField()
    typeContrat=models.CharField(max_length=20)
    user=models.ForeignKey(Utilisateur,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.typeContrat


class data_user(models.Model):
    prod=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    conso=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

class Accesory(models.Model):
    domotique=models.BooleanField()