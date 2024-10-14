from django.urls import path
from . import views

urlpatterns = [
    # Adicione suas rotas aqui, por exemplo:
    path('', views.cadastro, name='cadastro'),
    path('', views.coleta_dados_usuario, name='cadastro'),
    path('', views.sorteio_aluno, name= 'sorteio'),
    
]
