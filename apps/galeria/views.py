from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

# a view serve pra renderizar as páginas HTML, que são chamadas de templates

def verifica_usuario(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')

def verifica_formulario(form, request, operacao):
    if form.is_valid():
            form.save()
            if operacao == 'nova_imagem':
                messages.success(request, 'Nova fotografia cadastrada com sucesso!')
            else:
                messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')
    

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
        verifica_formulario(form, request, 'nova_imagem')
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id) # pega no banco de dados a fotografia com o ID passado
    form = FotografiaForms(instance=fotografia) # instance cria um formulario com as informacoes ja preenchidas
    
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        verifica_formulario(form, request, 'editar_imagem')
    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Imagem deletada com sucesso!')
    return redirect('index')