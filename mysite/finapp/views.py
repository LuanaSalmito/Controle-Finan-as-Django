from django.shortcuts import render
from django.http import HttpResponse
from .forms import CadastroForm
from finapp.models import Usuario
from django.contrib.auth.models import User


def index(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "finapp/index.html", context)

def entrar(request):
    return render(request, "finapp/entrar.html")

def cadastrar(request):
    formulario_cadastro= CadastroForm()
    return render(request, "finapp/cadastrar.html", {'formulario_cadastro': formulario_cadastro})

def inicio(request):
    return render(request, "finapp/inicio.html")