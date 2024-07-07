from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login),
    path('cadastro/', views.cadastro),
    path('form-cadastro/', views.form_cadastro, name="form-cadastro"),
]
