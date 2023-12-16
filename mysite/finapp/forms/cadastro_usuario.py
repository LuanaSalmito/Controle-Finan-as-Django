from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.Form):

    username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"placeholder": "Username:", "class": "form-control"}))
    nome = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"placeholder": "Nome", "class": "form-control"}))
    sobrenome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Sobrenome", "class": "form-control"}))
    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={"placeholder": "E-mail", "class": "form-control"}))
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs={"placeholder": "Data de nascimento", "type": "date", "class": "form-control"}))
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"placeholder": "Senha", "class": "form-control"}))
    confirmar_senha = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"placeholder": "Confirmar senha", "class": "form-control"}))



    genero_escolha = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outro', 'Outro'),
    ]
    genero = forms.ChoiceField(choices=genero_escolha, widget=forms.Select(attrs={"class": "form-control"}))

    def clean(self):

        super().clean()
        password = self.cleaned_data.get("password")
        confirmar_senha = self.cleaned_data.get("confirmar_senha")
        email = self.cleaned_data.get("email")

        if password != confirmar_senha:

            msg = "Erro ao confirmar senha."
            self.add_error("confirmar_senha", msg)


            if User.objects.filter(email=email).count() > 0:

                msg = "E-mail já cadastrado."
                self.add_error("email", msg)
