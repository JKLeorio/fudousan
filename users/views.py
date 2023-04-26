from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView

from users.forms import RegisterForm, UserUpdateForm
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': RegisterForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('estate_list')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'profile_update.html'
    queryset = get_user_model().objects.all()

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user_profile_update', kwargs={'pk': self.request.user.pk})
