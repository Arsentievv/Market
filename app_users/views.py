from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app_market.models import History
from app_users.forms import RegistrationForm
from app_users.models import Profile


class RegistrationView(generic.edit.CreateView):
    template_name = 'app_users/registration_form.html'
    success_url = reverse_lazy('main')
    form_class = RegistrationForm

    def form_valid(self, form):
        form = RegistrationForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            surname = form.cleaned_data.get('surname')
            phone_numb = form.cleaned_data.get('phone_numb')
            email = form.cleaned_data.get('phone_numb')
            if self.request.FILES:
                avatar = self.request.FILES['avatar']
                Profile.objects.create(
                    user=user, phone_numb=phone_numb, email=email, surname=surname, avatar=avatar,
                    first_name=first_name, last_name=last_name
                )
            else:
                Profile.objects.create(
                    user=user, phone_numb=phone_numb, email=email, surname=surname,
                    first_name=first_name, last_name=last_name
                )
            return super(RegistrationView, self).form_valid(form)


class Login(LoginView):
    template_name = 'app_users/login_form.html'


class Logout(LogoutView):
    next_page = '/app_market/main/'


class MyAcoountView(generic.DetailView):

    model = User
    template_name = 'app_users/profile_detail.html'
    context_object_name = 'user_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = History.objects.select_related().filter(user=self.request.user)
        return context


class ProfileUpdateView(generic.UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'surname', 'phone_numb',
              'email', 'avatar')
    template_name = 'app_users/update_profile.html'
    success_url = reverse_lazy('main')