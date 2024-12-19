from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Perfil(models.Model):
    # Relacionamento de um para um com o modelo User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    documento = models.FileField(upload_to='documentos/', null=True, blank=True)
    
    # Definição do status do perfil (pendente, aprovado, recusado)
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado')
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"{self.user.username} - {self.get_status_display()}"
    
    # Método para verificar se o perfil está aprovado
    def is_approved(self):
        return self.status == 'aprovado'
    
    # Método para verificar se o perfil está recusado
    def is_denied(self):
        return self.status == 'recusado'

    # Método para atualizar o status diretamente
    def update_status(self, new_status):
        if new_status in dict(self.STATUS_CHOICES):
            self.status = new_status
            self.save()
            return True
        return False

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

