from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name="home"),
    path('<int:client_id>/', views.cliente, name='cliente'),
]
