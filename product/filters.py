import django_filters
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from django import forms

from .models import *


class ProductFilter(django_filters.FilterSet):

    produttore = django_filters.ModelChoiceFilter(
        field_name="produttore", queryset=Manifacturer.objects.all())
    #frasi_h=django_filters.MultipleChoiceFilter(field_name="frasi_h", queryset=Hazard_Statement.objects.all())

    class Meta:
        model = Product
        fields = ['nome', 'cod', 'frasi_h', 'frasi_p',
                  'produttore', 'fornitore', 'fasi_produzione']
        labels = {'cod': 'Codice'}
        # {
        # 'nome': ['icontains'],
        # 'cod': ['iexact'],
        # }

        def __init__(self, *args, **kwargs):

            super(ProductFilter, self).__init__(*args, **kwargs)

            self.fields["fasi_produzione"].widget = CheckboxSelectMultiple()
            self.fields["fasi_produzione"].queryset = Fasi_produzione.objects.all()


class filterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nome', 'cod', 'frasi_h', 'frasi_p',
                  'produttore', 'fornitore', 'fasi_produzione', 'stato_arte']
        widgets = {
            'cod': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'frasi_p': forms.TextInput(attrs={'class': 'form-control'}),
            'frasi_h': forms.TextInput(attrs={'class': 'form-control'}),
            'produttore': forms.TextInput(attrs={'class': 'form-control'}),
            'fornitore': forms.TextInput(attrs={'class': 'form-control'}),
            'fasi_produzione': forms.TextInput(attrs={'class': 'form-control'}),
            'stato_arte': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Product2Filter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['nome', 'cod', 'frasi_h', 'frasi_p',
                  'produttore', 'fornitore', 'fasi_produzione', 'stato_arte']
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
