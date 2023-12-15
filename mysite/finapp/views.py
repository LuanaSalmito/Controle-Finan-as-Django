from django.shortcuts import render, redirect
#from django.http import HttpResponse
from mysite.finapp.forms import CadastroForm
from finapp.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


def index(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "finapp/index.html", context)


def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            
            user = User.objects.create_user(
                username=form.data["email"],
                email=form.data["email"],
                password=form.data["senha"],
                first_name=form.data["nome"],
                last_name=form.data["sobrenome"],
            )
            user.save()

            # Criar Usuário
            usuario = Usuario.objects.create(
                user=user,
                nome = form.data["nome"],
                sobrenome = form.data["sobrenome"],
                email=form.data["email"],
                cpf=form.data["cpf"],
                dataNascimento=form.data["dataNascimento"],
                cep=form.data["cep"],
                numero_residencia=form.data["numero_residencia"],
                complemento_residencia=form.data["complemento_residencia"],
                bairro=form.data["bairro"],
                rua=form.data["rua"],
                telefone=form.data["telefone"],
            )
            usuario.save()

            return redirect("entrar")
    else:
        form = CadastroForm()

    return render(request, "finapp/cadastre-se.html", {"form": form})


def entrar(request):
    login = "entrar"
    context = {"login": login}
    return render(request, "finapp/entrar.html", context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['senha']
        usuario = authenticate(username=email, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect("dashboard")
        else:
            messages.success(request, 'Email ou senha inválidos. Por favor, tente novamente.')
            return render(request, 'finapp/entrar.html')
    else:
        return redirect('entrar')



def dashboard(request):
     return render(request, "finapp/dashboard.html")