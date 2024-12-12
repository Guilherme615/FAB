from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('login/', views.login_view, name='login'),
<<<<<<< HEAD
    path('register/', views.register, name='register'),  # Renomeado de 'inscricao' para 'register'
    path('logout/', views.logout_view, name='logout'),  # URL para o logout
    path('editais/', views.editais, name='editais'),
    path('resultados/', views.resultados, name='resultados'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('candidato/', views.candidato, name='candidato')
]
=======
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),  # URL para o perfil
    path('profile_photo/', views.upload_profile_picture, name='profile_photo'),  # Corrigido duplicata
    path('cadastrar-obra/', views.cadastrar_obra, name='cadastrar_obra'),  # Nome correto
    path('listar-obras/', views.listar_obras, name='listar_obras'),
    path('editar-obra/<int:obra_id>/', views.editar_obra, name='editar_obra'),
    path('excluir-obra/<int:obra_id>/', views.excluir_obra, name='excluir_obra'),
    path('obra/<str:titulo>/', views.detalhes_obra, name='detalhes_obra'),
    path('solicitar-obra/', views.solicitar_obra, name='solicitar_obra'),
    path('minhas-solicitacoes/', views.minhas_solicitacoes, name='minhas_solicitacoes'),
    path('excluir_solicitacao/<int:id>/', views.excluir_solicitacao, name='excluir_solicitacao'),
    path('gerenciar-solicitacoes/', views.gerenciar_solicitacoes, name='gerenciar_solicitacoes'),
    path('confirmar-solicitacao/<int:solicitacao_id>/', views.confirmar_solicitacao, name='confirmar_solicitacao'),
    path('rejeitar-solicitacao/<int:solicitacao_id>/', views.rejeitar_solicitacao, name='rejeitar_solicitacao'),
    path('limpar_solicitacoes/', views.limpar_solicitacoes, name='limpar_solicitacoes'),
    path('opiniao/editar/<int:id>/', views.editar_opiniao, name='editar_opiniao'),
    path('opiniao/excluir/<int:id>/', views.excluir_opiniao, name='excluir_opiniao'),
    path('todas-as-obras/', views.todas_as_obras, name='todas_as_obras'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 5e9ebc0202526dd3e04a35ac43592f5ae7481ee8
