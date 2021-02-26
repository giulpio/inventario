from django.shortcuts import render, redirect
from django.http import HttpResponse

from product.models import Precautionary_Statement, Hazard_Statement


from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


class globalView(ListView):
    context_object_name = 'name'
    template_name = 'frasi_h_p/list.html'
    queryset = Precautionary_Statement.objects.all()
    orders = ['code']

    def get_context_data(self, **kwargs):
        context = super(globalView, self).get_context_data(**kwargs)
        context['frasi_h'] = Hazard_Statement.objects.all().order_by('code')
        context['frasi_p'] = Precautionary_Statement.objects.all().order_by('code')
        return context


class h_create(CreateView):
    model = Hazard_Statement
    template_name = 'frasi_h_p/create.html'
    fields = '__all__'


class h_update(UpdateView):
    model = Hazard_Statement
    template_name = 'frasi_h_p/create.html'
    fields = '__all__'


class h_delete(SuccessMessageMixin, DeleteView):
    model = Hazard_Statement
    success_url = '/frasi'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        code = self.object.code
        # name will be change according to your need
        request.session['code'] = code
        message = request.session['code'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)


class p_create(CreateView):
    model = Precautionary_Statement
    template_name = 'frasi_h_p/create.html'
    fields = '__all__'


class p_update(UpdateView):
    model = Precautionary_Statement
    template_name = 'frasi_h_p/create.html'
    fields = '__all__'


class p_delete(SuccessMessageMixin, DeleteView):
    model = Precautionary_Statement
    success_url = '/frasi'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        code = self.object.code
        # name will be change according to your need
        request.session['code'] = code
        message = request.session['code'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)
