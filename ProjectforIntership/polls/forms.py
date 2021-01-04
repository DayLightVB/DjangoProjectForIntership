from .models import Ad
from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['product_type',
                  'name',
                  'model',
                  'color',
                  'condition',
                  'price',
                  'place',
                  'description',
                  'photo']

        widgets = {
            'product_type': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product Type'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Model'
            }),
            'color': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Color'
            }),
            'condition': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Condition'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }),
            'place': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Place'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            'photo': FileInput(attrs={
                'class': 'form-control',
            }),
        }
