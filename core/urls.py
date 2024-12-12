from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),  # Renomeado de 'inscricao' para 'register'
    path('logout/', views.logout_view, name='logout'),  # URL para o logout
    path('editais/', views.editais, name='editais'),
    path('resultados/', views.resultados, name='resultados'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('candidato/', views.candidato, name='candidato')
]
