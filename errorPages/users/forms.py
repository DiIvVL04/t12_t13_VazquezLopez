from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'required': True,
        })
    )

    name = forms.CharField(
        label="Nombre completo",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre completo',
            'required': True,
        })
    )

    surname = forms.CharField(
        label="Apellido completo",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido completo',
            'required': True,
        })
    )

    control_number = forms.CharField(
        label="Número de control",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Número de control',
            'required': True,
        })
    )

    age = forms.CharField(
        label="Edad",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Edad',
            'required': True,
        })
    )

    tel = forms.CharField(
        label="Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Teléfono',
            'required': True,
        })
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'required': True,
        })
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
            'required': True,
        })
    )
    
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        pattern = r'^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$'
        if not re.match(pattern, email):
            raise forms.ValidationError("El correo debe pertenecer a la UTEZ.")
        return email

    def clean_control_number(self):
        control_number = self.cleaned_data.get("control_number")
        pattern = r'^[0-9]{5}tn[0-9]{3}$'
        if not re.match(pattern, control_number):
            raise forms.ValidationError("El número de control debe pertenecer a la UTEZ.")
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get("tel")
        pattern = r'^\d{10}$'
        if not re.match(pattern, tel):
            raise forms.ValidationError("El número telefónico debe ser de 10 digitos.")
        return tel

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        pattern = r'(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?]).{8,}'
        if not re.match(pattern, password):
            raise forms.ValidationError("La contraseña debe tener 8 caracteres, una letra mayúscula, un número y un carácter especial: (!#$%&?).")
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data
        
class CustomUserLoginForm(AuthenticationForm):
    pass