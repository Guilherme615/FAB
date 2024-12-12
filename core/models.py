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
