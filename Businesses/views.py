from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    clientes = Businesses.objects.all()
    context = {'clientes': clientes}
    return render(request, 'businesses/home.html', context)

def cliente(request, client_id):
    try:
        cliente = Businesses.objects.get(id = client_id)
    except:
        return render(request, 'businesses/home.html', context)

    context = {'cliente': cliente}
    return render(request, 'businesses/cliente.html', context)
