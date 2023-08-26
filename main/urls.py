from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'), #url da primeira pagina
    
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'), #url da segunda pagina
]
