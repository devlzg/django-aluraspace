# escrevendo os formularios do html utilizando python/django
from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu nome de usuário..."
            }
        )
    )
    
    senha_login = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha..."
            }
        )
    )
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Usuário: ',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu nome de usuário..."
            }
        )
    )
    
    email = forms.EmailField(
        label='E-mail: ',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu email..."
            }
        )
    )

    senha_cadastro1 = forms.CharField(
        label='Senha: ',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha..."
            }
        )
    )

    senha_cadastro2 = forms.CharField(
        label='Insira sua senha novamente: ',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente..."
            }
        )
    )