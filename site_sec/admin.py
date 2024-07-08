from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Perguntas)
admin.site.register(Certificado)


def cadastrar_usuario(nome, email, senha):
    novo_usuario = Usuario(nome=nome,email=email,senha=senha)
    novo_usuario.save()
    

def fazer_login(email):
    usuario = Usuario.objects.get(email=email)
    return usuario.senha

def buscar_perguntas(tipo):
    perguntas = Perguntas.objects.filter(tipo=tipo).order_by('?')[:10]
    return perguntas