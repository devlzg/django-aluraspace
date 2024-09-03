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
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserir espaços dentro desse campo.")
            else:
                return nome
    
    def clean_senha_cadastro2(self):
        senha_cadastro1 = self.cleaned_data.get("senha_cadastro1")
        senha_cadastro2 = self.cleaned_data.get("senha_cadastro2")

        if senha_cadastro1 and senha_cadastro2:
            if senha_cadastro1 != senha_cadastro2:
                raise forms.ValidationError("As senhas não são compatíveis.")
            else:
                return senha_cadastro2