from django import forms
from django.core.exceptions import ValidationError


class BalancoForm(forms.Form):
    nome = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"placeholder": "Nome do balanço", "class": "form-control"}))
    saldoInicio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={"class": "form-control"}))
    
    periodo_escolha = [
        ('15 dias', '15 dias'),
        ('30 dias', '30 dias'),
    ]
    periodo = forms.ChoiceField(choices=periodo_escolha, widget=forms.Select(attrs={"class": "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        saldoInicio = cleaned_data.get('saldoInicio')
        periodo = cleaned_data.get('periodo')
 
        if not nome:
            raise ValidationError('O nome não pode ser vazio.')
        
        if any(char.isdigit() for char in nome):
            raise ValidationError('O nome não pode conter números.')
        
        if saldoInicio <= 0:
            raise ValidationError('O saldo inicial deve ser um valor positivo.')
        
        if not periodo:
            raise ValidationError('O período não pode ser vazio.')


        return cleaned_data