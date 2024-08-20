from django.shortcuts import render
from galeria.models import Fotografia

# a view serve pra renderizar as páginas HTML, que são chamadas de templates
def index(request):
  fotografias = Fotografia.objects.all() # traz todos os itens do banco de dados
  return render(request, 'galeria/index.html', {"cards": fotografias}) # a requisição vai ser sempre o primeiro parametro, em seguida o arquivo HTML a ser renderizado

def imagem(request):
  return render(request, 'galeria/imagem.html')