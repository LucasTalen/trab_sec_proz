from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import FileResponse
from django.core.cache import cache
from .admin import *
from .funcoes import *
import json
import os
# Create your views here.
@csrf_exempt
def em_construcao(request):
    return HttpResponse("Em construção")

@csrf_exempt
def quiz_alunos(request):
    return render(request, 'site_sec/quiz_aluno.html')

@csrf_exempt
def login(request):
    return render(
        request,
        'site_sec/login.html'
    )
@csrf_exempt
def cadastro(request):
    return render(
        request,
        'site_sec/cadastrar.html'
    )

@csrf_exempt
def curso_aluno(request):
    return render(request, 'site_sec/curso_alunos.html')

@csrf_exempt
def index(request):
    return render(request, 'site_sec/index.html')

@csrf_exempt
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
    
@csrf_exempt 
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
    
@csrf_exempt
def check_user_email_cookie(request):
    email = request.COOKIES.get('user_email', 'Cookie not set')
    return HttpResponse(f"User Email Cookie: {email}")

@csrf_exempt
def prova_aluno(request):
    perguntas = buscar_perguntas("Aluno")
    perguntas_html = gerar_perguntas_html(perguntas)
    return render(request, 'site_sec/prova_aluno.html', {'perguntas': perguntas_html})

@csrf_exempt
def prova_professor(request):
    perguntas = buscar_perguntas("Professor")
    perguntas_html = gerar_perguntas_html(perguntas)
    print(perguntas_html)
    return render(request, 'site_sec/prova_aluno.html', {'perguntas': perguntas})

@csrf_exempt
def get_result_prova_aluno(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = request.COOKIES.get('email')
        
        gerar_nota_aluno(data,email)
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'fail'}, status=400)

@csrf_exempt
def baixar_certificado_aluno(request):
    email = request.COOKIES.get('email')
    usuario = Usuario.objects.get(email=email)
    emitir_certificado(usuario.nome)
    file_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', f'certificado_aluno_{usuario.nome}.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, content_type='application/pdf')


@csrf_exempt
def baixar_certificado_professor(request):
    email = request.COOKIES.get('email')
    usuario = Usuario.objects.get(email=email)
    emitir_certificado_professor(usuario.nome)
    file_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', f'certificado_professor_{usuario.nome}.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, content_type='application/pdf')



@csrf_exempt
def certificados(request):
    email = request.COOKIES.get('email')
    certificados_html = gerar_certificado_html(email)
    print(certificados_html)
    return render(request, 'site_sec/certificados.html', {'certificados': certificados_html})


@csrf_exempt
def quiz_professor(request):
    return render(request, 'site_sec/quiz_professor.html')