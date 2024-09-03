from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm): #ModelForm usa um model ja existente, enquanto Form cria uma nova
    class Meta: 
        model = Fotografia
        exclude = ['publicada'] # talvez tenha que colocar virgula pra funcionar, por ser uma lista
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de Registro',
            'usuario': 'Usuário'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control',
                                                                         'type': 'date'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }