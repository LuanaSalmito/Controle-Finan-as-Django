from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CadastroForm
from finapp.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "finapp/index.html", context)

def cadastrar(request):

    if request.method == "POST":
        form_cadastro = CadastroForm(request.POST)

        if form_cadastro.is_valid():
            user = User.objects.create_user(
                username=form_cadastro.cleaned_data['nome'],
                email=form_cadastro.cleaned_data['email'],
                password=form_cadastro.cleaned_data["senha"],
            )

            usuario = Usuario.objects.create(
                user=user,
                nome=form_cadastro.cleaned_data["nome"],
                sobrenome=form_cadastro.cleaned_data["sobrenome"],
                email=form_cadastro.cleaned_data["email"],
                dataNascimento=form_cadastro.cleaned_data["dataNascimento"],
                senha=form_cadastro.cleaned_data["senha"],
                genero=form_cadastro.cleaned_data["genero"],
            )

            usuario.save()

            return redirect("entrar")
        
    else:
        form_cadastro = CadastroForm()

    return render(request, "finapp/cadastrar.html", {"form_cadastro": form_cadastro})


# def entrar(request):
#     if request.method == "POST":
#         form_login = LoginForm(request.POST)

#         if form_login.is_valid():
#             email = form_login.cleaned_data['email']
#             senha = form_login.cleaned_data['senha']

#             user = authenticate(request, username=email, password=senha)

#             if user is not None:
#                 login(request, user)
#                 return redirect("dashboard")  
#             else:
#                 # Usuário não autenticado, trate conforme necessário
#                 # Exemplo: Adicionar uma mensagem de erro ao formulário
#     # else:
#     #     form_login = LoginForm()

#             return render(request, "finapp/entrar.html", {"form_login": form_login})


# @login_required
# def dashboard(request):
#     return render(request, "finapp/dashboard.html")