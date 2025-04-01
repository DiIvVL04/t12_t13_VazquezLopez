from django import forms
from .models import Alumno

#Podemos crear un formulario para cada modelo que exista
class alumnoForm(forms.ModelForm):
    #La clase meta (Metainfo del formulario)
    class Meta:

        #Definir de que modelo se basa el formulario
        model = Alumno

        #Definir que campos van a ser incluidos en el formulario
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']

        #Definir como se deben de ver o que atributos tienen los campos
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido del alumno'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad del alumno'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Matricula del alumno'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo del alumno'
                }
            ),
        }

        #Etiquetas/Labels personalizadas
        labels={
            'nombre': 'Nombre del alumno',
            'apellido': 'Apellido del alumno',
            'edad': 'Edad del alumno',
            'matricula': 'Matricula del alumno',
            'correo': 'Correo del alumno'
        }

        #Mensajes de error personalizados
        error_messages={
            'nombre': {
                'required': 'El nombre es obligatorio'
                },
            'matricula': {
                'unique': 'La matricula debe ser única'
                },
            'correo': {
                'unique': 'El correo debe ser único'
                }
        }