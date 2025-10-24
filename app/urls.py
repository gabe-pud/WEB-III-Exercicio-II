from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('sobre', views.sobre, name='sobre'),
    path('desenvolvedores', views.dev, name='dev'),
    path('excluir-dev/<int:id_dev>', views.excluirDev, name='excluirDev'),
    path('salvar-dev', views.salvarDev, name='salvarDev'),
    path('editar-dev/<int:id_dev>', views.editarDev, name='editarDev'),


    path('contatos', views.contato, name='contato'),
    path('salvar-contato', views.salvarContato, name='salvarContato'),
    path('excluir-contato/<int:id_contato>', views.excluirContato, name='excluirContato'),



]
