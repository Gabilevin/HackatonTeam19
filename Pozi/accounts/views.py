from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.views import UserModel
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse
from django.views import View

from .form import RegistrationForm, register_extra, EmailChangeForm
from .models import regiter_extra_model, User
from django.contrib.auth import authenticate, login, logout
from .decorators import unatenticated_user
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect("basic_app:index")
    else:
        if request.method == "POST":
            form = RegistrationForm(request.POST or None)
            form1 = register_extra(request.POST or None)
            if form.is_valid() and form1.is_valid():
                user = form.save()
                # default to non-active
                user.is_active = False
                user.save()
                profile = form1.save(commit=False)
                profile.user = user

                if 'image' in request.FILES:
                    profile.image = request.FILES['image']
                profile.save()
                user1 = form1.save()
                group = Group.objects.get(name='customer')
                user.groups.add(group)

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

                domain = get_current_site(request).domain
                link = reverse('accounts:activate',
                               kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})
                email_subject = 'Activate your account'
                activate_url = 'http//' + domain + link
                email_body = 'Hi ' + user.username + 'Please use this link to verfy your account\n' + activate_url

                email = EmailMessage(
                    email_subject,
                    email_body,
                    'rafulhelp@gmail.com',
                    [user.email],
                )

                email.send(fail_silently=False)
                username = form.cleaned_data['username']
                raw_password = form.cleaned_data.get('password1')
                #
                user = authenticate(username=user.username, password=raw_password)
                return redirect("basic_app:index")

        else:
            form = RegistrationForm()
            form1 = register_extra()
        return render(request, "accounts/register.html", {"form": form, "form1": form1})


class VerificationView(View):
    def get(self, request, uidb64, token):
        return redirect('accounts:login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "accounts/activate.html")
    else:
        return HttpResponse('Activation link is invalid!')


@unatenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("basic_app:index")
            else:
                return render(request, 'accounts/login.html', {"error": "your account has been disabled or not "
                                                                    "activated yet"})
        else:
            return render(request, 'accounts/login.html', {"error": "invalid Username or Password.try again."})
    return render(request, 'accounts/login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("accounts:login")
    else:
        return redirect("accounts:login")


def change_email(request):
    form = EmailChangeForm()
    if request.method == 'POST':
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            user = request.user
            user.email = form.cleaned_data['email']
            user.save()
        return redirect("basic_app:index")

    return render(request, 'accounts/change_email.html', {'form': form})
