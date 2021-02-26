from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import test

from .forms import TestForm

from .filters import *

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


class test_list(ListView):
    model = test
    template_name = 'tests/list.html'
    ordering = ['product__cod']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TestFilter(
            self.request.GET, queryset=self.get_queryset())
        #context['json_data'] = json.dumps(list(Product.objects.values()))
        return context


class test_detail(DetailView):
    model = test
    template_name = 'tests/detail.html'


class create_test(CreateView):
    model = test
    template_name = 'tests/create.html'
    fields = '__all__'


class test_update(UpdateView):
    model = test
    template_name = 'tests/create.html'
    fields = '__all__'


class test_delete(SuccessMessageMixin, DeleteView):
    model = test
    success_url = '/tests'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        # name will be change according to your need
        request.session['name'] = name
        message = request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)
