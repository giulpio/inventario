import django_filters
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from django import forms

from product.models import *


class filterForm(forms.ModelForm):
    class Meta:
        model = test
        fields = ['ap_apeo', 'clorobenzeni_clorutolenti', 'clorofenoli',
                  'ammine_aromatiche', 'coloranti_dispersi', 'coloranti_cancerogeni', 'navy_blue',
                  'ritardanti_fiamma', 'glicoli', 'solventi', 'organostannici', 'idricarburi_policiclici_aromatici', 'voc',
                  'ftalati', 'pfc', 'metalli_pesanti', 'product', 'scadenza_rapporto']
        widgets = {
            'ap_apeo': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'clorobenzeni_clorutolenti': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'clorofenoli': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'ammine_aromatiche': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'coloranti_dispersi': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'coloranti_cancerogeni': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'navy_blue': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'ritardanti_fiamma': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'glicoli': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'solventi': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'organostannici': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'idricarburi_policiclici_aromatici': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'voc': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'ftalati': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'pfc': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'metalli_pesanti': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class TestFilter(django_filters.FilterSet):
    class Meta:
        model = test
        fields = ['ap_apeo', 'clorobenzeni_clorutolenti', 'clorofenoli',
                  'ammine_aromatiche', 'coloranti_dispersi', 'coloranti_cancerogeni', 'navy_blue',
                  'ritardanti_fiamma', 'glicoli', 'solventi', 'organostannici', 'idricarburi_policiclici_aromatici', 'voc',
                  'ftalati', 'pfc', 'metalli_pesanti', 'product', 'scadenza_rapporto']

        # ap_apeo = django_filters.BooleanFilter(
        #   name='online', lookup_expr='isnull')

        form = filterForm

        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            # models.BooleanField: {
            #     'filter_class': django_filters.BooleanFilter,
            #     'extra': lambda f: {
            #         'widget': forms.CheckboxInput,
            #     },
            # },
        }
