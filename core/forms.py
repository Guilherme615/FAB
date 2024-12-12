from django import forms
from .models import Inscricao, Edital
from django.utils import timezone  # Importando timezone para pegar a data atual

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome', 'cpf', 'email', 'telefone', 'documento', 'termos']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu CPF'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu e-mail'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu telefone'}),
            'documento': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'termos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nome de Usuário',
        widget=forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'})
    )
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha', 'class': 'form-control'})
    )

class EditalForm(forms.ModelForm):
    class Meta:
        model = Edital
        fields = ['titulo', 'descricao', 'data_publicacao', 'arquivo_pdf', 'status']  # Adapte conforme o seu modelo