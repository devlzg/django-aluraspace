from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

# a view serve pra renderizar as páginas HTML, que são chamadas de templates

def verifica_usuario(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')

def index(request):
    verifica_usuario(request)
    fotografias = Fotografia.objects.order_by(
        "-data_fotografia").filter(publicada=True)  # traz todos os itens do banco de dados
    # a requisição vai ser sempre o primeiro parametro, em seguida o arquivo HTML a ser renderizado
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    # passando pro html um dicionario com uma instancia do banco de dados
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    fotografias = Fotografia.objects.order_by(
        "-data_fotografia").filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    verifica_usuario(request)
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada com sucesso!')
            return redirect('index')
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass