from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Certificado(models.Model):
    TIPO_CHOICES = [
        ('Aluno', 'Aluno'),
        ('Professor', 'Professor'),
    ]
    id_usuario_certificado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return f'{self.tipo} - {self.id_usuario_certificado}'

class Perguntas(models.Model):
    TIPO_CHOICES = [
        ('Aluno', 'Aluno'),
        ('Professor', 'Professor'),
    ]
    pergunta_index = models.TextField(blank=True, null=True)
    RESPOSTA_CHOICES = [
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
        ('d', 'd'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    pergunta = models.TextField()
    resposta = models.CharField(max_length=1, choices=RESPOSTA_CHOICES)

    def __str__(self):
        return self.pergunta