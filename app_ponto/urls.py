from django.urls import path
from . import views
from app_ponto.views import *

from django.contrib.auth import views as auth_views



urlpatterns=[
    #path('',Registro,name='encontratag'),
    path('login/sucesso/',login_sucesso, name='login_sucesso'),
    path('',user_login,name="login_inicial"),
    path('login/',user_login,name='login'),
    path('sair/',logout_user,name='logout'),
]