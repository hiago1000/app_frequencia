from django.shortcuts import render, redirect
from django.views.generic import ListView,TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import *
from datetime import datetime, time
import socket
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.



def Registro(request,id):
    id=int(id)
    data_atual = datetime.now()
    hora_em_texto = data_atual.strftime('%H:%M:%S')
    data_em_texto=data_atual.strftime('%Y-%m-%d')
    funcionario1=Funcionario.objects.get(usuario__id__exact=id)
    idFuncionario=funcionario1.id
    frequen=Frequencia.objects.filter(fucionario__id__exact=idFuncionario)
    frequencias=None
    for i in frequen:
        if str(i.data) == data_em_texto:
            frequencias=i
    if frequencias == None:
        frequencias=Frequencia(data=data_em_texto,fucionario=funcionario1,ipCom=socket.gethostbyname(socket.gethostname()))
    if frequencias.horario_entrada_1 == None:
        frequencias.horario_entrada_1=hora_em_texto
    elif frequencias.horario_saida_1 == None:
        frequencias.horario_saida_1=hora_em_texto
    elif frequencias.horario_entrada_2 == None:
        frequencias.horario_entrada_2=hora_em_texto
    elif frequencias.horario_saida_2 == None:
        frequencias.horario_saida_2=hora_em_texto
    frequencias.save()
    html='''
    '''
    return HttpResponse(html)

@login_required(login_url='http://localhost:8000/')
def login_sucesso(request):
    return render(request, 'app_ponto/login_sucesso.html')

def logout_user(request):
    logout(request)
    return redirect("http://localhost:8000/")

def user_login(request):
    if request.method == "POST":

        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('Senha')
        user = authenticate(username=str(username), password=str(password))
        if user is not None:
            if user.is_active:
                print(user.id)
                login(request, user)
                Registro('',user.id)
                return redirect(login_sucesso)
            else:
                return HttpResponse("Usuário desativado")
                # Retorna uma mensagem de erro de 'conta desabilitada' .
        else:
            messages.error(request,'Login ou senha invalidos. Tente Novamente')
            # Retorna uma mensagem de erro 'login inválido'.
    else:
        form = LoginForm()
    return render(request, 'app_ponto/login.html', {'form': form})