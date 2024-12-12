from django.db import models
from datetime import date

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
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('fechado', 'Fechado'),
    ]
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_publicacao = models.DateField()
    arquivo_pdf = models.FileField(upload_to='editais/', null=True, blank=True, default='path/to/default/file.pdf')  # Definindo um arquivo padrão
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='aberto')

    def __str__(self):
        return self.titulo

