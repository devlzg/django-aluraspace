from django.shortcuts import render

# a view serve pra renderizar as páginas HTML, que são chamadas de templates
def index(request):
  dados = {
  1: {"nome": "Nebulosa de Carina",
      "legenda": "webtelescope.org / NASA / James Webb"},
  2: {"nome": "Galáxia NGC 1079",
      "legenda": "nasa.org / NASA / Hubble"}
}
  
  return render(request, 'galeria/index.html', {"cards": dados}) # a requisição vai ser sempre o primeiro parametro, em seguida o arquivo HTML a ser renderizado

def imagem(request):
  return render(request, 'galeria/imagem.html')