from django.shortcuts import render, redirect
from finapp.forms.cadastro_usuario import CadastroForm
from finapp.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required





# Página de início:

def index(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "finapp/index.html", context)



# Cadastro:

def cadastro(request):

    if request.method == "POST":

        form = CadastroForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.data["email"],
                password=form.data["password"],
                first_name=form.data["nome"],
                last_name=form.data["sobrenome"],
            )
            user.save()

            # Criar Usuário
            usuario = Usuario.objects.create(
                user=user,
                nome=form.data["nome"],
                sobrenome=form.data["sobrenome"],
                email=form.data["email"],
                data_nascimento=form.data["data_nascimento"],
                genero=form.data["genero"],
            )
            usuario.save()

            return redirect("entrar")

    else:
        form = CadastroForm()

    return render(request, "finapp/cadastrar.html", {"form": form})





# Views login e logout:

def entrar(request):
    login = "entrar"
    context = {"login": login}
    return render(request, "finapp/entrar.html", context)



def usuario_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        usuario = authenticate(username=email, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect("dashboard")
        else:
            messages.success(request, 'Email ou senha inválidos. Por favor, tente novamente.')
            return render(request, 'finapp/entrar.html')
    else:
        return redirect('entrar')



def usuario_logout(request):

    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Você saiu com sucesso. Até logo!')
    return redirect('index')




# Pagina inicial pós autenticação

@login_required
def dashboard(request):
     return render(request, "finapp/dashboard.html")




















































# from django.shortcuts import render, redirect
# from .forms import CadastroForm
# from finapp.models import Usuario
# from django.contrib.auth.models import User
# from django.contrib import messages
# # from django.contrib.auth import authenticate, login, logout



# def index(request):
#     temp = "temporário"
#     context = {"temp": temp}
#     return render(request, "finapp/index.html", context)

# def cadastrar(request):

#     if request.method == "POST":
#         form_cadastro = CadastroForm(request.POST)

#         if form_cadastro.is_valid():
#             user = User.objects.create_user(
#                 username=form_cadastro.cleaned_data['nome'],
#                 email=form_cadastro.cleaned_data['email'],
#                 password=form_cadastro.cleaned_data["senha"],
#             )

#             usuario = Usuario.objects.create(
#                 user=user,
#                 nome=form_cadastro.cleaned_data["nome"],
#                 sobrenome=form_cadastro.cleaned_data["sobrenome"],
#                 email=form_cadastro.cleaned_data["email"],
#                 dataNascimento=form_cadastro.cleaned_data["dataNascimento"],
#                 senha=form_cadastro.cleaned_data["senha"],
#                 genero=form_cadastro.cleaned_data["genero"],
#             )

#             usuario.save()

#             return redirect("entrar")

#     else:
#         messages.error(request, 'Formulário inválido, preencha novamente.')
#         return redirect("cadastrar")

#     return render(request, "finapp/cadastrar.html", {"form_cadastro": form_cadastro})


# def entrar(request):
#     login = "entrar"
#     context = {"login": login}
#     return render(request, "finapp/entrar.html", context)

# # def usuario_login(request):
# #     if request.method == 'POST':
# #         email = request.POST['email']
# #         password = request.POST['senha']
# #         usuario = authenticate(username=email, password=password)

# #         if usuario is not None:
# #             login(request, usuario)
# #             return redirect("dashboard")
# #         else:
# #             messages.error(request, 'Email ou senha inválidos. Por favor, tente novamente.')
# #             return redirect('entrar')

# #     else:
# #         return redirect('entrar')

# # def sair(request):
# #     if request.user.is_authenticated:
# #         logout(request)
# #     return redirect('index')



# def dashboard(request):
#     dash = "dash"
#     context = {"dash": dash}
#     return render(request, "finapp/dashboard.html", context)


