from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import pandas as pd
import numpy as np
from .models import *
from Businesses.models import *
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'GET':
        tipos = CompensationTypes.objects.all()
        clientes = Businesses.objects.all()
        compensacoes = ['1/3 Férias',
                    'Anuênio',
                    'Férias indenizadas',
                    '15 dias auxilio doença',
                    'Aviso prévio indenizado',
                    'Abono de férias',
                    'Vale transporte',
                    'Auxílio creche'
                       ]
        context = {
            'compensation_types': tipos,
            'compensacoes': compensacoes,
            'clientes': clientes,
        }
        return render(request, 'compensacoes/compensacao.html', context)
    if request.method == "POST":
        compensacao = Compensations()
        compensacao.name = request.POST['nome']
        compensacao.tipo = CompensationTypes.objects.get(id = request.POST['tipo'])
        compensacao.cliente = Businesses.objects.get(id =
                                                    request.POST['cliente'])
        compensacao.pdf = request.FILES['arquivo'] 
        compensacao.date_start = datetime.now()
        compensacao.date_end = datetime.now()
        compensacao.save()
        
        #arq = request.FILES['arquivo']
        #f = pd.read_csv(arq)
        #f.columns = ['valor', 'mes']

        clientes = Businesses.objects.all()

        context = {
            'clientes': clientes,
        }

        return render(request, 'businesses/home.html', context)
