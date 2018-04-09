from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name="home"),
    path('clientes/<int:client_id>/', views.cliente, name='cliente'),
]
