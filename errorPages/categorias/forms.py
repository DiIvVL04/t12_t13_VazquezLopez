from django import forms
from .models import Categoria

#Podemos crear un formulario para cada modelo que exista
class categoriaForm(forms.ModelForm):
    #La clase meta (Metainfo del formulario)
    class Meta:

        #Definir de que modelo se basa el formulario
        model = Categoria

        #Definir que campos van a ser incluidos en el formulario
        fields = ['nombre', 'imagen']

        #Definir como se deben de ver o que atributos tienen los campos
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la categoria'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL de la categoria'
                }
            )
        }

        #Etiquetas/Labels personalizadas
        labels={
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la categoria'
        }

        #Mensajes de error personalizados
        error_messages={
            'nombre': {'required': 'El nombre es obligatorio'}
        }