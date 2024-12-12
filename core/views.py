from django.shortcuts import render, redirect
from .forms import InscricaoForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        email = request.POST['email']
        telefone = request.POST['telefone']
        documento = request.FILES['documento']
        termos = request.POST.get('termos')
        senha = request.POST['senha']  # Obter a senha do formulário

        if termos:
            # Criar o usuário no banco de dados
            user = User.objects.create_user(username=nome, email=email, password=senha)  # Usar "nome" como username
            user.first_name = nome  # Armazenar o nome completo no campo `first_name`
            user.save()

            # Processar o documento (opcional)
            # Salve o documento de alguma forma, se necessário

            # Exibir a mensagem de sucesso
            return render(request, 'inscricao.html', {'success': True})
        else:
            return render(request, 'inscricao.html', {'error': 'Você precisa aceitar os termos para se inscrever.'})

    return render(request, 'inscricao.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # O "username" agora é o "nome"
            senha = form.cleaned_data['senha']
            
            # Autenticar o usuário
            user = authenticate(request, username=username, password=senha)
            
            if user is not None:
                login(request, user)
                return redirect('candidato')  # Ajuste para a URL desejada
            else:
                form.add_error(None, 'Nome ou senha inválidos.')  # Mensagem de erro ajustada
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  # Desloga o usuário
    return redirect('index')  # Redireciona para a página inicial (substitua 'home' pela URL desejada)

def editais(request):
    return render(request, 'editais.html')

def resultados(request):
    # Filtra todos os usuários, mas exclui o administrador
    usuarios = User.objects.exclude(is_superuser=True)
    return render(request, 'resultados.html', {'usuarios': usuarios})

def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')

def candidato(request):
    return render(request, 'area-candidato.html')