from django.shortcuts import render, redirect, get_object_or_404
from .forms import InscricaoForm, LoginForm, EditalForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Edital, HistoricoEditais, Perfil
from django.core.paginator import Paginator
from django.utils import timezone  # Importando timezone para pegar a data atual
from django.contrib.auth.decorators import login_required


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
        senha = request.POST['senha']

        if termos:
            # Criar o usuário no banco de dados
            user = User.objects.create_user(username=nome, email=email, password=senha)  
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
    return redirect('index')  # Redireciona para a página inicial

def resultados(request):
    # Filtra todos os usuários, mas exclui o administrador
    usuarios = User.objects.exclude(is_superuser=True)
    return render(request, 'resultados.html', {'usuarios': usuarios})

def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')

@login_required
def candidato(request):
    return render(request, 'area-candidato.html', {'user': request.user})


def cadastrar_edital(request):
    if request.method == 'POST':
        form = EditalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('editais')  # Nome de uma página de listagem futura
    else:
        form = EditalForm()
    return render(request, 'cadastrar_edital.html', {'form': form})

def edital_view(request):
    editais_list = Edital.objects.all().order_by('-data_publicacao')  # Ordenar por data
    paginator = Paginator(editais_list, 10)  # 10 editais por página
    page_number = request.GET.get('page')
    editais = paginator.get_page(page_number)
    return render(request, 'editais.html', {'editais': editais})

@login_required
def excluir_edital(request, edital_id):
    if not request.user.is_staff:
        messages.error(request, "Você não tem permissão para excluir editais.")
        return redirect('editais.html')

    edital = get_object_or_404(Edital, id=edital_id)
    edital.delete()
    messages.success(request, "Edital excluído com sucesso.")
    return redirect('editais')

@login_required
def inscrever_edital(request, edital_id):
    edital = get_object_or_404(Edital, id=edital_id)
    
    if edital.status.lower() != 'aberto':
        messages.error(request, "O edital não está mais aberto para inscrições.")
        return redirect('listar_editais')  # Ajuste o nome da sua URL para listar editais

    # Adicionar o edital ao histórico do usuário
    historico, created = HistoricoEditais.objects.get_or_create(user=request.user, edital=edital)
    if created:
        messages.success(request, "Você se inscreveu com sucesso no edital!")
    else:
        messages.warning(request, "Você já está inscrito nesse edital.")
    
    return redirect('listar_editais')

def listar_editais(request):
    editais = Edital.objects.all()
    return render(request, 'listar_editais.html', {'editais': editais})

def aprovar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)
    
    # Tenta pegar o perfil do usuário ou cria um novo caso não exista
    perfil, created = Perfil.objects.get_or_create(user=usuario)
    
    # Atualiza o status do perfil para aprovado
    perfil.status = 'aprovado'
    perfil.save()
    
    # Redireciona para a página de resultados ou qualquer outra página que desejar
    return redirect('resultados')  # ou 'resultados' caso queira voltar para a lista

def recusar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    # Verifica se o usuário tem um perfil associado
    try:
        perfil = usuario.perfil  # Acessa o perfil do usuário
        perfil.status = 'recusado'  # Altera o status para 'recusado'
        perfil.save()  # Salva as alterações
        messages.success(request, f"Usuário {usuario.get_full_name()} recusado com sucesso.")
    except Perfil.DoesNotExist:
        messages.error(request, "Perfil não encontrado para o usuário.")
    
    return redirect('resultados')

@login_required
def resultado_edital(request):
    # Obtém o perfil do usuário logado
    perfil = Perfil.objects.filter(user=request.user).first()
    
    if perfil:
        # Verifica se o usuário tem histórico de inscrições
        historico_editais = perfil.user.historico_editais.all()
    else:
        historico_editais = []

    return render(request, 'resultado_edital.html', {
        'perfil': perfil,
        'historico_editais': historico_editais,
    })

@login_required
def documentos(request):
    # Obtém o perfil do usuário logado
    perfil = Perfil.objects.filter(user=request.user).first()

    if perfil:
        # Recupera os dados do perfil, como nome, email, e o documento carregado
        nome = perfil.user.first_name
        email = perfil.user.email
        documento = perfil.documento  # Supondo que 'documento' seja o campo do arquivo
    else:
        nome = email = documento = None

    return render(request, 'documentos.html', {
        'perfil': perfil,
        'nome': nome,
        'email': email,
        'documento': documento,
    })