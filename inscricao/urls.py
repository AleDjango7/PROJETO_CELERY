from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscricao, name='inscricao'),
    path('processa_inscricacao', views.processa_inscricacao, name='processa_inscricacao'),

]
