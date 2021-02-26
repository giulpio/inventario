from django.shortcuts import render, redirect
from django.http import HttpResponse

from product.models import Pictogram_dpi, Pictogram_h

from .forms import *

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


class globalView(ListView):
    context_object_name = 'name'
    template_name = 'pittogrammi/list.html'
    queryset = Pictogram_h.objects.all()

    def get_context_data(self, **kwargs):
        context = super(globalView, self).get_context_data(**kwargs)
        context['pittogrammi_h'] = Pictogram_h.objects.all()
        context['pittogrammi_d'] = Pictogram_dpi.objects.all()
        return context


class h_create(CreateView):
    model = Pictogram_h
    template_name = 'pittogrammi/create.html'
    form_class = pittogrammi_h_form
    # fields='__all__'


class h_update(UpdateView):
    model = Pictogram_h
    template_name = 'pittogrammi/create.html'
    form_class = pittogrammi_h_form
    # fields='__all__'


class h_delete(SuccessMessageMixin, DeleteView):
    model = Pictogram_h
    success_url = '/pittogrammi'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        # name will be change according to your need
        request.session['name'] = name
        message = request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)


class p_create(CreateView):
    model = Pictogram_dpi
    template_name = 'pittogrammi/create.html'
    fields = '__all__'


class p_update(UpdateView):
    model = Pictogram_dpi
    template_name = 'pittogrammi/create.html'
    fields = '__all__'


class p_delete(SuccessMessageMixin, DeleteView):
    model = Pictogram_dpi
    success_url = '/pittogrammi'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        # name will be change according to your need
        request.session['name'] = name
        message = request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)
