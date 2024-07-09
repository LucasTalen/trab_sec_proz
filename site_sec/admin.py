from django.contrib import admin
from .models import *
from django import forms
# Register your models here.


class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Perguntas
        fields = '__all__'
        widgets = {
            'pergunta_index': forms.Textarea(attrs={'cols': 99, 'rows': 1}),
        }

class PerguntaAdmin(admin.ModelAdmin):
    fields = ['tipo', 'pergunta_index', 'pergunta', 'resposta']
    form = PerguntaForm
    
    
admin.site.register(Usuario)
admin.site.register(Perguntas, PerguntaAdmin)
admin.site.register(Certificado)


def cadastrar_usuario(nome, email, senha):
    novo_usuario = Usuario(nome=nome,email=email,senha=senha)
    novo_usuario.save()
    

def fazer_login(email):
    usuario = Usuario.objects.get(email=email)
    return usuario.senha

def buscar_perguntas(tipo):
    perguntas = Perguntas.objects.filter(tipo=tipo).order_by('?')[:10].values('pergunta_index', 'pergunta')
    return perguntas

def buscar_resposta(pergunta):
    print("per:", pergunta)
    resposta = Perguntas.objects.filter(pergunta_index=pergunta).values('resposta')
    print('--', list(resposta))
    return resposta