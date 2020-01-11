from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView, ListView,
    CreateView, UpdateView, DeleteView, DetailView
)
from core.models import Business, Country, City, Comment, User, Review, MyUser


def index(request):
    countries_list = Country.objects.all()
    cities_list = City.objects.all()
    business_list = Business.objects.all()
    filt1 = request.GET.get('countries')
    if filt1:
        filt1 = int(filt1)
        cities_list = cities_list.filter(country__pk=filt1)
    filt2 = request.GET.get('cities')
    if filt2:
        filt2 = int(filt2)
        business_list = business_list.filter(city__pk=filt2)
    return render(request, 'index.html',
                  {'business_list': business_list,
                   'cities_list': cities_list,
                   'countries_list': countries_list, 'filt1': filt1, 'filt2': filt2})


class BusinessView(DetailView):
    template_name = 'business_profile.html'
    context_object_name = 'business'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        business = Business.objects.get(id=self.kwargs['pk'])
        data['comments'] = business.comments.all()
        reviews_list = business.reviews.all()
        rate = 0
        for review in reviews_list:
            rate = rate + review.rating
        rate = float(rate / len(reviews_list))
        data['rate'] = rate
        return data

    def get_object(self):
        business = Business.objects.get(id=self.kwargs['pk'])
        return business

class CreateReviewView(CreateView):
    model = Review
    fields = ['rating']

    def form_valid(self, form):
        business = Business.objects.get(id=self.kwargs['pk'])
        Review.objects.create(
            created_by=self.request.user,
            business=business,
            **form.cleaned_data
        )
        return redirect(reverse_lazy("business_detail", kwargs={"pk": self.kwargs['pk']}))

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']


    def form_valid(self, form):
        business = Business.objects.get(id=self.kwargs['pk'])
        Comment.objects.create(
            user=self.request.user,
            business=business,
            **form.cleaned_data
        )
        return redirect(reverse_lazy("business_detail",
                                     kwargs={"pk": self.kwargs['pk']}))


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
