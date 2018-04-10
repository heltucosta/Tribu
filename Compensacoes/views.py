from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import pandas as pd
import numpy as np
from .models import *

# Create your views here.
def index(request):
    if request.method == 'GET':
        tipos = CompensationTypes.objects.all()
        compensacoes = ['1/3 Férias',
                    'Anuênio',
                    'Férias indenizadas',
                    '!5 dias auxilio doença',
                    'Aviso prévio indenizado',
                    'Abono de férias',
                    'Vale transporte',
                    'Auxílio creche'
                       ]
        context = {
            'compensation_types': tipos,
            'compensacoes': compensacoes,
        }
        return render(request, 'compensacoes/compensacao.html', context)
    if request.method == "POST":
        compensacao = Compensations()
        compensacao.name = request.POST['nome']
        compensacao.tipo = CompensationTypes.objects.get(name =
                                                         request.POST['tipo'])
        compensacao.arquivo = request.FILES['arquivo'] 
        #arq = request.FILES['arquivo']
        #f = pd.read_csv(arq)
        #f.columns = ['valor', 'mes']
        return render(request, 'businesses/home.html', {})
