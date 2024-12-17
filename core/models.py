from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Inscricao(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    documento = models.FileField(upload_to='documentos/')
    termos = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Edital(models.Model):
    titulo = models.CharField(max_length=255)
    data_publicacao = models.DateField()
    status = models.CharField(max_length=50, choices=(('Aberto', 'Aberto'), ('Fechado', 'Fechado')))
    arquivo_pdf = models.FileField(upload_to='editais/', null=True, blank=True)
    data_publicacao = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class HistoricoEditais(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historico_editais')
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE, related_name='inscricoes')
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.edital.titulo}"

