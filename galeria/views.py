from django.shortcuts import render

# a view serve pra renderizar as páginas HTML, que são chamadas de templates
def index(request):
  return render(request, 'galeria/index.html') # a requisição vai ser sempre o primeiro parametro, em seguida o arquivo HTML a ser renderizado

def imagem(request):
  return render(request, 'galeria/imagem.html')