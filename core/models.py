from django.db import models

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
    descricao = models.TextField(blank=True)
    arquivo_pdf = models.FileField(upload_to='editais/', verbose_name="Arquivo PDF")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo