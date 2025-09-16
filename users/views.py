from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LogoutView

class Login(LoginView):
    authentication_form = LoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return '/dashboard/role-redirect/'

class Logout(LogoutView):
    next_page = '/'  # redirect after logout
    def get(self, request, *args, **kwargs):
        """Allow GET request logout (not recommended for production security)"""
        return self.post(request, *args, **kwargs)

class Register(View):
    def get(self, request):
        return render(request, 'users/register.html', {'form': RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('role-redirect')
        return render(request, 'users/register.html', {'form': form})
