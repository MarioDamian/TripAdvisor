from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView,
    CreateView, UpdateView, DeleteView, DetailView
)
from django.views import View

from core.models import MyUser


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    model = MyUser

    def form_valid(self, form):
        data = form.cleaned_data
        user = MyUser.objects.create_user(username=data['username'],
                                          password=data['password'])
        return redirect('home')

class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self):
        form = AuthenticationForm()
        return {'form': form}

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            return render(request, "login.html", {"form": form})

class LogoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('home'))