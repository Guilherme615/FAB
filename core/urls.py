from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),  # Registro de usuários
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('editais/', views.edital_view, name='editais'),  # Página de editais (geral)
    path('editais/listar/', views.listar_editais, name='listar_editais'),  # Lista de editais detalhada
    path('editais/cadastrar/', views.cadastrar_edital, name='cadastrar_edital'),  # Cadastro de edital
    path('editais/excluir/<int:edital_id>/', views.excluir_edital, name='excluir_edital'),  # Excluir edital
    path('editais/inscrever/<int:edital_id>/', views.inscrever_edital, name='inscrever_edital'),  # Inscrever-se em edital
    path('resultados/', views.resultados, name='resultados'),  # Resultados
    path('about/', views.about, name='about'),  # Sobre
    path('feedback/', views.feedback, name='feedback'),  # Feedback
    path('candidato/', views.candidato, name='candidato'),  # Área do candidato
    path('aprovar/<int:usuario_id>/', views.aprovar_usuario, name='aprovar_usuario'),  # Aprovar usuário
    path('recusar/<int:usuario_id>/', views.recusar_usuario, name='recusar_usuario'),  # Recusar usuário
    path('resultado_edital/', views.resultado_edital, name='resultado_edital'),
    path('documentos/', views.documentos, name='documentos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
