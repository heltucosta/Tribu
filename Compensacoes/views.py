from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponse
from .models import *
import pandas as pd
import numpy as np
from .models import *
from Businesses.models import *
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from Tribu import settings
import os
from weasyprint import HTML, CSS

# Create your views here.
def index(request):
    ###########
    ### GET ###
    ###########
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

    ############
    ### POST ###
    ############
    if request.method == "POST":

        # Arquivo de compensacao nao anexado
        if not request.FILES:
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
                'error': "Arquivo obrigatorio"
            }

            return render(request, 'compensacoes/compensacao.html', context)

        # leitura do arquivo CSV
        df = pd.read_csv(request.FILES['arquivo'])
        df.columns=['valor', 'mes']
        # Parse de datas iniciais e finais da compensacao
        compensationStartDate = datetime.strptime("01/"+df.mes[df.index[0]], '%d/%m/%Y')
        compensationEndDate = datetime.strptime("01/"+df.mes[df.index[-1]], '%d/%m/%Y')

        # filtro de selics para periodo da compensacao
        selics = Selic.objects.filter(period__gte =
                                      compensationStartDate,
                                      period__lte =
                                      compensationEndDate)

        # iniciado array que alimentara tabela do PDF
        compensationArrays = pd.DataFrame(columns=['Mês/Ano',
                                                   request.POST['nome'],
                                                   '%INSS', 'Valor', 'Selic',
                                                   'Total'])

        # realizado calculo de compensacao mensal por selic
        compensacaoTotal, INSSTotal, CalculoTotal = 0, 0, 0
        for idx, selic in enumerate(selics):
            strDate = selic.period.strftime("%b/%y")
            numDate = selic.period.strftime("%m/%Y")
            valor = df.valor[idx]
            valorINSS = valor*0.2
            total = valorINSS + valorINSS * selic.value.__float__()/100.0

            compensacaoTotal += valor
            INSSTotal += valorINSS
            CalculoTotal += total

            # Compensacao intermediaria
            newCompensation = pd.DataFrame([
                [strDate, 
                 valor,
                 20.00,
                 valorINSS,
                 selic.value,
                 total]
            ], columns = compensationArrays.columns.tolist())

            # total de compensacoes
            compensationArrays = compensationArrays.append(newCompensation)

        compensacao = Compensations()
        compensacao.name = request.POST['nome']
        compensacao.tipo = CompensationTypes.objects.get(id = request.POST['tipo'])
        compensacao.cliente = Businesses.objects.get(id =
                                                    request.POST['cliente'])
        compensacao.date_start = datetime.now()
        compensacao.date_end = datetime.now()


        context = {
            'compensacao': compensacao,
            'compensations': compensationArrays,
            'total': [compensacaoTotal, INSSTotal, CalculoTotal]
        }

        css = "body{ \
                    margin: 40px 10%; \
                } \
                body, h4, p { \
                    text-align: center; \
                } \
                table { \
                    width: 100%; \
                    border-spacing: 0; \
                } \
                thead > tr { \
                    background-color: lightgray; \
                    line-height: 30px;\
                } \
                thead, tr, th { \
                    border-bottom: 2px solid black; \
                } \
                tbody, tr { \
                    line-height: 30px; \
                } \
                tr:last-child { \
                    background-color: lightgray; \
                } \
                tbody, th { \
                    border-top: 2px solid black; \
                }"

        pdf = render_to_string('pdf.html', context)

        HTML(string=pdf.encode('utf-8')).write_pdf('compensacao.pdf',
                                          stylesheets=[CSS(string=css)])

        f = open('compensacao.pdf', 'rb')

        compensacao.pdf.save("{}{}.pdf".format(compensacao.cliente.name,
                                           compensacao.date_start), File(f))
        compensacao.save()

        clientes = Businesses.objects.all()

        context = {
            'clientes': clientes,
            'alert': 'Compensação enviada'
        }

        f.close()

        return render(request, 'businesses/home.html', context)

def pdf_view(request, compensation_id):
    try:
        compensation = Compensations.objects.get(id = compensation_id)
    except:
        context = {
            'message': 'Compensação não encontrada.'
        }

        return render(request, 'businesses/home.html', context)

    with open(compensation.pdf.path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
 #       response['Content-Disposition'] = 'inline; filename='+compensation.pdf
        return response
    pdf.closed
