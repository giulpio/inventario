from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *

from .forms import *

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from .filters import ProductFilter, Product2Filter

import json


class product_delete(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = '/'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        nome = self.object.nome
        # name will be change according to your need
        request.session['nome'] = nome
        message = request.session['nome'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)


class product_update(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/create.html'
    # fields = '__all__'


class product_create(CreateView):
    model = Product
    template_name = 'product/create.html'
    fields = '__all__'

# aggiunto get_absolute_url in models


class product_detail(DetailView):
    model = Product
    template_name = 'product/product.html'
    fields = '__all__'


class product_list(ListView):
    model = Product
    template_name = 'product/home.html'
    ordering = ['cod']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Product2Filter(
            self.request.GET, queryset=self.get_queryset())
        #context['json_data'] = json.dumps(list(Product.objects.values()))
        return context


def createProduct(request):
    form = ProductForm(request.GET or None)
    formset = SostanzeFormset(queryset=Concentrazioni.objects.none())
    if request.method == 'POST':
        form = ProductForm(request.POST)
        #formset = SostanzeFormset(request.POST)
        # if form.is_valid() and formset.is_valid():
        if form.is_valid():
            product = form.save()
            # for f in formset:
            #    sostanza = f.save(commit=False)
            #    sostanza.product = product
            #    sostanza.save()
        return redirect('/')

    context = {'form': form, 'formset': formset}

    return render(request, 'product/create.html', context)


def update(self, request, *args, **kwargs):
    self.object = self.get_object()
    # form_class = self.get_form_class()
    form = ProductForm(request.GET)
    qs = models.Concentrazioni.objects.filter(product=self.get_object())
    formset = forms.SostanzeFormset(self.request.POST, queryset=qs)

    if form.is_valid():
        product = form.save()
        # for f in formset:
        #   sostanza = f.save(commit=False)
        #   sostanza.product = product
        #   sostanza.save()
    return redirect('/')

    context = {'form': form, 'formset': formset}

    return render(request, 'product/create.html', context)


# sostituito dalla vista product_list
# def home(request):

#     context = {
#         'products': Product.objects.all(),
#     }
#     return render(request, 'product/home.html', context)


# def index(request):
#     return render(request, 'product/index.html')


def ajax_change_status(request):
    active = request.GET.get('active', False)
    product_id = request.GET.get('r_id', False)
    print(request.GET.get('r_id'))
    print(active)
    # first you get your Job model
    product = Product.objects.get(pk=product_id)
    print(product)
    try:
        product.stato_arte = active
        product.save()
        print("eccomi")
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False})
    return JsonResponse(data)
