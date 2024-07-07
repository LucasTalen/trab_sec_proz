from django.shortcuts import render
from django.http import HttpResponse
from .admin import cadastrar_usuario, fazer_login


# Create your views here.
def em_construcao(request):
    return HttpResponse("Em construção")


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
    email = request.POST.get('nome')
    senha = request.POST.get('senha')
    senha_usuario = ''
    
    try:
        senha_usuario = fazer_login(email)
    except:
        print("Usuario não existe")
        
    if senha == senha_usuario:
        return render(request, 'site_sec/index.html')