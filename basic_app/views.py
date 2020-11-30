from django.shortcuts import render
from .forms import UserForm #UserProfileInfoForm
from django.views.generic import View
from pyexpat.errors import messages
from django.views import View
from .models import Activation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string
from .forms import UserForm, ChangeEmailForm  # UserProfileInfoForm
from django.views.generic import FormView
from django.contrib.auth.views import (PasswordChangeView as BasePasswordChangeView,)
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class ChangePasswordView(BasePasswordChangeView):
    template_name = 'profile/change_password.html'

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request,'Your password was changed.')

        return redirect('basic_app:change_password')


class ChangeEmailView(LoginRequiredMixin, FormView):
    template_name = 'basic_app/profile/change_email.html'
    form_class = ChangeEmailForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        user = self.request.user
        email = form.cleaned_data['email']

        if settings.ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE:
            code = get_random_string(20)

            act = Activation()
            act.code = code
            act.user = user
            act.email = email
            act.save()

            send_activation_change_email(self.request, email, code)

            messages.success(self.request, 'To complete the change of email address, click on the link sent to it.')
        else:
            user.email = email
            user.save()

            messages.success(self.request, _('Email successfully changed.'))

        return redirect('accounts:change_email')


def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def settings(request):
    return HttpResponse("You in Settings! :D")

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid(): #and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)#,profile_form.errors)
    else:
        user_form = UserForm()
        #profile_form = UserProfileInfoForm()
    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,

                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They: used username {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'basic_app/login.html',{})