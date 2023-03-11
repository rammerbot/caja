from django.shortcuts import render
from django.views.generic import FormView, View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


from .forms import LoginForm
from applications.users.models import User
# Create your views here.

class LoginView(FormView):

    template_name = "users/login.html"
    form_class = LoginForm                                            
    success_url = reverse_lazy('informes_app:date')

    def form_valid(self, form):
        user =  authenticate(
            username = form.cleaned_data['user'],
            password = form.cleaned_data['password'],
        ) 
        login(self.request, user)

        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    
    def get(self, request, *args, **kwargs):

        logout(request)

        return HttpResponseRedirect(reverse('users_app:login'))