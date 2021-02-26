from django import forms
from django.forms import ModelForm
from django.forms import modelformset_factory
from django.forms.formsets import formset_factory
from .models import *


class SosForm(ModelForm):
    class Meta:
        model = Concentrazioni
        fields = '__all__'


CFormset = formset_factory(SosForm)


class ProductForm(forms.ModelForm):
    sostanze = CFormset()

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            #    'nome': forms.TextInput(attrs={'class': 'form-control'}),
            #    'classe': forms.TextInput(attrs={'class': 'form-control'}),
            #    'fornitore': forms.Select(attrs={'class': 'form-control'}),
            #    'cod': forms.TextInput(attrs={'class': 'form-control'}),
            #    'produttore': forms.Select(attrs={'class': 'form-control'}),
            'mod_stoccaggio': forms.Textarea(attrs={'class': 'form-textfield'}),
            #    'tds': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            #    'sds': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            #    'note_zdhc': forms.Textarea(attrs={'class': 'form-control'}),
            #    'certificazioni': forms.SelectMultiple(attrs={'class': 'form-control'}),
            #    'conf_zdhc': forms.CheckboxInput(),
            #    'frasi_h': forms.SelectMultiple(attrs={'class': 'form-control'}),
            #    'frasi_p': forms.SelectMultiple(attrs={'class': 'form-control'}),
            #    'pittogrammi_hazard': forms.SelectMultiple(attrs={'class': 'form-control'}),
            #    'pittogrammi_dpi': forms.SelectMultiple(attrs={'class': 'form-control'}),
            #    'fasi_produzione': forms.SelectMultiple(attrs={'class': 'form-control'}),
            #    'stato_arte': forms.Select(attrs={'class': 'form-control'}),
            #    'gateway': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'sds_date': forms.DateInput(attrs={'class': 'vDateField'})
        }


SostanzeFormset = modelformset_factory(
    Concentrazioni,
    fields=('name', 'concentrazione',),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
        'class': 'form-control',
        # 'placeholder': 'Enter Author Name here'
    })
    }
)
