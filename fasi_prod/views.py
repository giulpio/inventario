from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse

from product.models import Fasi_produzione


from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


class fasi_list(ListView):
    model = Fasi_produzione
    template_name = 'fasi_prod/list.html'
    fields = '__all__'


class update(UpdateView):
    model = Fasi_produzione
    template_name = 'fasi_prod/create.html'
    fields = '__all__'


class create(CreateView):
    model = Fasi_produzione
    template_name = 'fasi_prod/create.html'
    fields = '__all__'
    success_url = '/fasi'


class delete(SuccessMessageMixin, DeleteView):
    model = Fasi_produzione
    success_url = '/fasi'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        # name will be change according to your need
        request.session['name'] = name
        message = request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)
