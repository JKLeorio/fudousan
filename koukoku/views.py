from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from .forms import EstateCreationForm
from .models import Estate


class HomeView(TemplateView):
    template_name = 'home.html'


class EstateCreateView(LoginRequiredMixin, CreateView):
    template_name = 'estate_create.html'
    form_class = EstateCreationForm
    success_url = reverse_lazy('estate_list')


class EstateListView(ListView):
    template_name = 'estate_list.html'
    model = Estate
    context_object_name = 'estates'


class EstateDetailView(DetailView):
    model = Estate
    template_name = 'estate_detail.html'


class EstateUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'estate_update.html'
    form_class = EstateCreationForm
    model = Estate
    success_url = reverse_lazy('estate_list')
