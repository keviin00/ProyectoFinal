from django import forms
from .models import CustomUser

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'nombre', 'password', 'direccion']
