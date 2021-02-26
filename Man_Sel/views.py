from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse

from product.models import Manifacturer, Seller


from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin


class globalView(ListView):
    context_object_name = 'name'
    template_name = 'Man_Sel/list.html'
    queryset = Manifacturer.objects.all()

    def get_context_data(self, **kwargs):
        context = super(globalView, self).get_context_data(**kwargs)
        context['produttori'] = Manifacturer.objects.all()
        context['venditori'] = Seller.objects.all()
        return context


class m_create(CreateView):
    model = Manifacturer
    template_name = 'Man_Sel/create.html'
    fields = '__all__'
    success_url = '/man_sel'


class m_update(UpdateView):
    model = Manifacturer
    template_name = 'Man_Sel/create.html'
    fields = '__all__'


class m_delete(SuccessMessageMixin, DeleteView):
    model = Manifacturer
    success_url = '/man_sel'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        # name will be change according to your need
        request.session['name'] = name
        message = request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)


class s_create(CreateView):
    model = Seller
    template_name = 'Man_Sel/create.html'
    fields = '__all__'
    success_url = '/man_sel'


class s_update(UpdateView):
    model = Seller
    template_name = 'Man_Sel/create.html'
    fields = '__all__'


class s_delete(SuccessMessageMixin, DeleteView):
    model = Seller
    success_url = '/man_sel'
    success_message = "deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        # name will be change according to your need
        request.session['name'] = name
        message = request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)
