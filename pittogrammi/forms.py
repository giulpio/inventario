from django import forms
from django.forms import ModelForm
from django.forms import modelformset_factory
from django.forms.formsets import formset_factory
from product.models import *


class pittogrammi_h_form(forms.ModelForm):
    class Meta:
        model = Pictogram_h
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-image'}),

        }
