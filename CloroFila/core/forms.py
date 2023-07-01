from django import forms
from django.forms import ModelForm
from .models import *


class ProductoForm(ModelForm):

    class Meta:
        model = producto
        fields = ['nombre','precio','descripcion','stock','exterior','categoria','fecha_germinacion','stock','imagen']

class CategoriaForm(ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'

