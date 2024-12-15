from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),  # Renomeado de 'inscricao' para 'register'
    path('logout/', views.logout_view, name='logout'),  # URL para o logout
    path('editais/', views.edital_view, name='editais'),
    path('resultados/', views.resultados, name='resultados'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('candidato/', views.candidato, name='candidato'),
    path('cadastrar/', views.cadastrar_edital, name='cadastrar_edital'),
    path('excluir-edital/<int:edital_id>/', views.excluir_edital, name='excluir_edital'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
