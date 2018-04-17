from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index, name='compensacao'),
    path('visualizar/<int:compensation_id>/', views.pdf_view, name='pdf')

]
