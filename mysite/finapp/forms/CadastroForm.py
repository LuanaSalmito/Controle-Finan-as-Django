from django import forms
from django.contrib.auth.models import User


class CadastroForm(forms.Form):

    nome = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"placeholder": "Nome"}))

    sobrenome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Sobrenome"}))

    email = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"placeholder": "E-mail"}))
    
    dataNascimento = forms.DateField(widget=forms.TextInput(attrs={"placeholder": "Data de nascimento", "type": "date"}))

    senha = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"placeholder": "Senha"}))

    confirmar_senha = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"placeholder": "Confirmar senha"}))


    genero_escolha = [
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outro', 'Outro'),
    ]
    genero = forms.ChoiceField(choices=genero_escolha, widget=forms.Select(attrs={}))

    
    def clean(self):
        
        super().clean()

        senha = self.cleaned_data.get("senha")
        confirmar_senha = self.cleaned_data.get("confirmar_senha")
        email = self.cleaned_data.get("email")

        if senha != confirmar_senha:
            msg = "Erro ao confirmar senha."
            self.add_error("confirmar_senha", msg)
        
        if User.objects.filter(email=email).count() > 0:
            msg = "E-mail já cadastrado."
            self.add_error("email", msg)