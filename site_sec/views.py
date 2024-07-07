from django.shortcuts import render
from django.http import HttpResponse


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
