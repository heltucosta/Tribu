from django.contrib import admin
from django.urls import path, include
from Businesses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index) ,
    path('reajuste/', include('Compensacoes.urls')),
    path('clientes/', include('Businesses.urls')),
]
