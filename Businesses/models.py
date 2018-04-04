from django.db import models

# Create your models here.
class Businesses(models.Model):
    name = models.CharField('Nome Fantasia', max_length=200)
    cnpj = models.CharField('CNPJ', max_length = 200)
    razao_social = models.CharField('Razão Social', max_length = 200)
    endereco = models.CharField('Endereço', max_length = 200)
    telefone = models.CharField('Telefone', max_length = 200)
    email = models.EmailField('E-mail', max_length=254)

