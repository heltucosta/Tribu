from django.db import models

# Create your models here.
class Compensations(models.Model):
    name = models.CharField('Compensação', max_length=200)
    date_start = models.DateField('Data de início')
    date_end = models.DateField('Data fim')

class CompensationTypes(models.Model):
    name = models.CharField('Tipo de compensação', max_length=200)

class Selic(models.Model):
    value = models.DecimalField('Valor', max_digits = 12, decimal_places = 2)
    period = models.DateTimeField('Período')
