from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from .admin import *
from .funcoes import *
import json


# Create your views here.
def em_construcao(request):
    return HttpResponse("Em construção")


def quiz_alunos(request):
    return render(request, 'site_sec/quiz_aluno.html')


def login(request):
    return render(
        request,
        'site_sec/login.html'
    )

def cadastro(request):
    return render(
        request,
        'site_sec/cadastrar.html'
    )

def curso_aluno(request):
    return render(request, 'site_sec/curso_alunos.html')

def index(request):
    return render(request, 'site_sec/index.html')

def form_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get("senha")
        senha_novamente = request.POST.get('senha_novamente')
        
        if senha == senha_novamente:
            cadastrar_usuario(nome,email,senha)
        
        return render(request, 'site_sec/login.html')
       
    else:
        return render(request, 'site_sec/cadastrar.html')
    
def form_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha_usuario = ''
    
    try:
        senha_usuario = fazer_login(email)
        response = render(request, 'site_sec/index.html')
        response.set_cookie('email', email, max_age=None, path='/')
        
        request.session['email'] = email
        request.session.modified = True
        
    except:
        print("Usuario não existe")
        
    if senha == senha_usuario:
        return response
    else:
        return HttpResponse(f"senha bd: {senha_usuario}, sua senha: {senha}, email: {email}")
    

def check_user_email_cookie(request):
    email = request.COOKIES.get('user_email', 'Cookie not set')
    return HttpResponse(f"User Email Cookie: {email}")

def prova_aluno(request):
    perguntas = buscar_perguntas("Aluno")
    perguntas_html = gerar_perguntas_html(perguntas)
    return render(request, 'site_sec/prova_aluno.html', {'perguntas': perguntas_html})

def prova_professor(request):
    perguntas = buscar_perguntas("Professor")
    perguntas_html = gerar_perguntas_html(perguntas)
    print(perguntas_html)
    return render(request, 'site_sec/prova_aluno.html', {'perguntas': perguntas})

def get_result_prova_aluno(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = request.COOKIES.get('email')
        
        gerar_nota_aluno(data,email)
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'fail'}, status=400)