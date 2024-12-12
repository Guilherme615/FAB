from django.shortcuts import render, redirect
from .forms import InscricaoForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


<<<<<<< HEAD
def index(request):
    return render(request, 'index.html')
=======
# Página inicial
class IndexView(View):
    def get(self, request):
        # Pega todas as obras cadastradas
        obras = Obra.objects.all()
        
        # Embaralha as obras e pega as 10 primeiras
        random_obras = random.sample(list(obras), min(len(obras), 10))
        
        return render(request, 'index.html', {'obras': random_obras})
>>>>>>> 5e9ebc0202526dd3e04a35ac43592f5ae7481ee8

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

<<<<<<< HEAD
def candidato(request):
    return render(request, 'area-candidato.html')
=======
# Página de perfil
def profile(request):
    user_profile = request.user.profile
    if not user_profile.photo:
        user_profile.photo = 'profile_photos/default_profile.png'
    return render(request, 'profile.html', {'user': request.user})

# Detalhes da obra
def detalhes_obra(request, titulo):
    obra = Obra.objects.filter(titulo=titulo).first()

    if not obra:
        obra = Obra.objects.create(titulo=titulo, capa=f"{titulo}.jpg")

    opinioes = Opiniao.objects.filter(obra=obra).order_by('-data_criacao')

    if request.method == "POST":
        if "texto" in request.POST:
            # Se for uma opinião nova
            usuario = request.user
            texto = request.POST.get("texto")
            if usuario and texto:
                Opiniao.objects.create(obra=obra, usuario=usuario.username, texto=texto)

        elif "delete_opiniao_id" in request.POST:
            # Se for para excluir uma opinião
            opiniao_id = request.POST.get("delete_opiniao_id")
            opiniao = Opiniao.objects.filter(id=opiniao_id, usuario=request.user.username).first()
            if opiniao:
                opiniao.delete()
            # Depois de excluir, redirecionar para a página de detalhes da obra
            return redirect('detalhes_obra', titulo=obra.titulo)

    return render(request, 'opiniao.html', {'obra': obra, 'opinioes': opinioes})

# Cadastro de obra
def cadastrar_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redireciona para a página inicial
    else:
        form = ObraForm()
    return render(request, 'cadastrar_obra.html', {'form': form})

# Listagem de obras
def listar_obras(request):
    obras = list(Obra.objects.all())
    random.shuffle(obras)  # Embaralha as obras
    return render(request, 'listar_obras.html', {'obras': obras})


# Edição de obra
def editar_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('listar_obras')
    else:
        form = ObraForm(instance=obra)
    return render(request, 'editar_obra.html', {'form': form})

# Exclusão de obra
def excluir_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    if request.method == 'POST':
        obra.delete()
        return redirect('listar_obras')
    return render(request, 'confirmar_exclusao.html', {'obra': obra})

@login_required
def solicitar_obra(request):
    if request.method == 'POST':
        form = SolicitacaoObraForm(request.POST)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.usuario = request.user
            solicitacao.save()
            return redirect('minhas_solicitacoes')
    else:
        form = SolicitacaoObraForm()
    return render(request, 'solicitar_obra.html', {'form': form})


@login_required
def minhas_solicitacoes(request):
    solicitacoes = SolicitacaoObra.objects.filter(usuario=request.user)
    return render(request, 'minhas_solicitacoes.html', {'solicitacoes': solicitacoes})


@login_required# Apenas administradores
def gerenciar_solicitacoes(request):
    solicitacoes = SolicitacaoObra.objects.all()
    return render(request, 'gerenciar_solicitacoes.html', {'solicitacoes': solicitacoes})


@login_required # Apenas administradores
def confirmar_solicitacao(request, solicitacao_id):
    solicitacao = get_object_or_404(SolicitacaoObra, id=solicitacao_id)
    solicitacao.status = 'Aprovada',
    solicitacao.save()
    return redirect('gerenciar_solicitacoes')

@login_required # Apenas administradores
def rejeitar_solicitacao(request, solicitacao_id):
    solicitacao = get_object_or_404(SolicitacaoObra, id=solicitacao_id)
    solicitacao.status = 'Recusada',
    solicitacao.save()
    return redirect('gerenciar_solicitacoes')

@login_required
def limpar_solicitacoes(request):
    # Verifica se o usuário é administrador
    if not request.user.is_superuser:
        raise PermissionDenied
    
    # Limpa todas as solicitações
    SolicitacaoObra.objects.all().delete()

    # Redireciona de volta para a página de gerenciamento de solicitações
    return redirect('gerenciar_solicitacoes')

@login_required
def excluir_solicitacao(request, id):
    # Verifica se o usuário é o proprietário da solicitação ou administrador
    solicitacao = get_object_or_404(SolicitacaoObra, id=id, usuario=request.user)

    # Exclui a solicitação
    solicitacao.delete()

    # Redireciona de volta para a página de Minhas Solicitações
    return redirect('minhas_solicitacoes')

@login_required
def editar_opiniao(request, id):
    opiniao = get_object_or_404(Opiniao, id=id, usuario=request.user)
    if request.method == "POST":
        novo_texto = request.POST.get("texto", "").strip()
        if novo_texto:
            opiniao.texto = novo_texto
            opiniao.save()
            return redirect('detalhes_obra', titulo=opiniao.obra.titulo)
    return render(request, 'editar_opiniao.html', {'opiniao': opiniao})

@login_required
def excluir_opiniao(request, id):
    opiniao = get_object_or_404(Opiniao, id=id, usuario=request.user)
    if request.method == "POST":
        opiniao.delete()
        return redirect('detalhes_obra', titulo=opiniao.obra.titulo)
    return render(request, 'excluir_opiniao.html', {'opiniao': opiniao})

def todas_as_obras(request):
    obras = Obra.objects.all()
    return render(request, 'todas_as_obras.html', {'obras': obras})
>>>>>>> 5e9ebc0202526dd3e04a35ac43592f5ae7481ee8
