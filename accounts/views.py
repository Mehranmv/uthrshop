# django imports
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# third party imports
from verify_email.email_handler import send_verification_email
# local imports
from .forms import UserCreationForm, UserLoginForm
from .models import User


class UserRegisterView(View):
    form_class = UserCreationForm

    def get(self, request):
        context = {
            'form': self.form_class()
        }
        return render(request, 'accounts/user_register.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            return redirect('pages:shop_page')
        return redirect('accounts:accounts_login')


class UserLoginView(View):
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, 'accounts/user_login.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.filter(email=cd['email'])
            if user.exists() and user.first().is_active:
                print('=' * 100)
                user = authenticate(request, email=cd['email'], password=cd['password'])
                login(request, user)
                return redirect('pages:index_page')
            elif not user:
                messages.error(request, 'There is no account with this email', 'danger')
                return redirect('accounts:accounts_login')
            else:
                messages.error(request, 'Your account is not active ! please check your email', 'danger')
                return redirect('accounts:accounts_login')
        return redirect('accounts:accounts_login')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('pages:index_page')


class UserProfileView(View):
    def get(self, request):
        return render(request, 'pages/my-account.html')
