from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#def index(request):
#    return redirect('/agenda/')
def login_user(request):
    return render(request,'login.html')

def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/agenda/')

@login_required(login_url='/login/')
def lista_eventos(request):
    #evento = Evento.objects.get(id=1)
    usuario = request.user
    #evento = Evento.objects.all()
    evento = Evento.objects.filter(usuario=usuario)
    #response = {'evento' :  evento}
    dados = {'eventos' : evento}
    return render(request, 'agenda.html', dados)

