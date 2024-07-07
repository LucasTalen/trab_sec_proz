from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login),
    path('cadastro/', views.cadastro),
    path('form-cadastro/', views.form_cadastro, name="form-cadastro"),
    path('form-login/', views.form_login, name="form-login"),
    path('check-user-email-cookie/', views.check_user_email_cookie, name='check_user_email_cookie'),
]
