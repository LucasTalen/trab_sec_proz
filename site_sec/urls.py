from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('cadastro/', views.cadastro),
    path('curso/aluno/', views.curso_aluno),
    path('form-cadastro/', views.form_cadastro, name="form-cadastro"),
    path('form-login/', views.form_login, name="form-login"),
    path('quiz-aluno/', views.quiz_alunos, name="quizz-aluno"),
    path('submit/prova/aluno/', views.get_result_prova_aluno, name="get-result-prova-aluno"),
    path('check-user-email-cookie/', views.check_user_email_cookie, name='check_user_email_cookie'),
    path('prova/aluno/', views.prova_aluno, name='prova-aluno'),

]
