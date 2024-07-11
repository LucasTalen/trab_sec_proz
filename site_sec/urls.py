from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('cadastro/', views.cadastro),
    path('curso/aluno/', views.curso_aluno),
    path('curso/professor/', views.curso_professor),
    path('form-cadastro/', views.form_cadastro, name="form-cadastro"),
    path('form-login/', views.form_login, name="form-login"),
    path('quiz-aluno/', views.quiz_alunos, name="quizz-aluno"),
    path('quiz-professor/', views.quiz_professor, name="quizz-professor"),
    path('submit/prova/aluno/', views.get_result_prova_aluno, name="get-result-prova-aluno"),
    path('submit/prova/professor/', views.get_result_prova_professor, name="get-result-prova-professor"),
    path('check-user-email-cookie/', views.check_user_email_cookie, name='check_user_email_cookie'),
    path('prova/aluno/', views.prova_aluno, name='prova-aluno'),
    path('prova/professor/', views.prova_professor, name='prova-professor'),
    path('baixar/aluno/', views.baixar_certificado_aluno, name='download_pdf'),
    path('baixar/professor/', views.baixar_certificado_professor, name='download_pdf_professor'),
    path('certificados/', views.certificados, name='pagina_certificados'),
    
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)