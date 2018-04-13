from django.db import models
from Businesses.models import *
from .models import *

# Create your models here.
class Compensations(models.Model):
    name = models.CharField('Compensação', max_length=200)
    date_start = models.DateField('Data de início')
    date_end = models.DateField('Data fim')
    cliente = models.ForeignKey(Businesses, on_delete=models.CASCADE)
    tipo = models.ForeignKey("CompensationTypes", on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='compensacoes')

    def __str__(self):
        return self.name

class CompensationTypes(models.Model):
    name = models.CharField('Tipo de compensação', max_length=200)

class Selic(models.Model):
    value = models.DecimalField('Valor', max_digits = 12, decimal_places = 2)
    period = models.DateField('Período')
