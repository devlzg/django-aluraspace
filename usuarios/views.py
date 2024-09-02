from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
	form = LoginForms()
 
	if request.method == 'POST':
		form = LoginForms(request.POST)

		if form.is_valid():
			nome = form['nome_login'].value()
			senha = form['senha_login'].value()

		usuario = auth.authenticate( # autenticacao que verifica se as credenciais estao corretas
			request,
			username = nome,
			password = senha
		)
		if usuario is not None: # autoriza o login
			auth.login(request, usuario)
			messages.success(request, f'{nome} logado com sucesso!')
			return redirect('index')
		else:
			messages.error(request, 'Erro ao efetuar o login')
			return redirect('login')


	return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
	form = CadastroForms()
  
	if request.method == 'POST':
		form = CadastroForms(request.POST)
  
	if form.is_valid():
		nome = form['nome_cadastro'].value() # pega os valores do formulario
		email = form['email'].value()
		senha = form['senha_cadastro1'].value()
  
		if User.objects.filter(username=nome).exists(): # verifica dentro da tabela de usuarios se há um usuario com este nome
			messages.error(request, 'Este usuário já existe.')
			return redirect('cadastro')

		usuario = User.objects.create_user( # cria o usuario com os valores do formulario
			username=nome,
			email=email,
			password=senha
		)
		usuario.save() # salva o novo usuario no banco de dados
		messages.success(request, f'Usuario {nome} cadastrado com sucesso!')
		return redirect('login')

	return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')