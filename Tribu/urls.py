from django.contrib import admin
from django.urls import path, include
from Businesses import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index) ,
    path('reajuste/', include('Compensacoes.urls')),
    path('clientes/', include('Businesses.urls')),
]
