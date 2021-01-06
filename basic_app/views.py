from pyexpat.errors import messages
from django.core.mail import send_mail, BadHeaderError
from .models import Activation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string
from .forms import UserForm, ChangeEmailForm, UserProfileInfoForm, ContactForm
from django.views.generic import FormView
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .utils import send_activation_change_email


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'basic_app/settings/Profile/change_password.html', {
        'form': form
    })


class ChangeEmailView(LoginRequiredMixin, FormView):
    template_name = 'basic_app/settings/change_email.html'
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

            messages.success(self.request, 'Email successfully changed.')

        return redirect('basic_app:change_email')


def index(request):
    return render(request, 'basic_app/index.html')


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
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and UserProfileInfoForm.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, UserProfileInfoForm.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'basic_app/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They: used username {} and password: {}".format(username, password))
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'basic_app/login.html', {})


def consultation(request):
    return render(request, 'basic_app/Menu/consultation.html', {})


def cost_chat(request):
    return render(request, 'basic_app/Menu/Chat/cost_chat.html', {})


def free_chat(request):
    return render(request, 'basic_app/Menu/Chat/free_chat.html', {})


def stories(request):
    return render(request, 'basic_app/Menu/stories.html', {})


def font_changing(request):
    return render(request, 'basic_app/settings/font_changing.html', {})


def Videos(request):
    return render(request, 'basic_app/Menu/Videos.html', {})


def Sport(request):
    return render(request, 'basic_app/Menu/videos/Sport.html', {})


def stand_up_comedy(request):
    return render(request, 'basic_app/Menu/videos/stand_up_comedy.html', {})


def motivation(request):
    return render(request, 'basic_app/Menu/videos/motivation.html', {})


def about(request):
    return render(request, 'basic_app/settings/about.html', {})


def QA(request):
    return render(request, 'basic_app/Menu/Chat/QA.html', {})


def Profile(request):
    return render(request, 'basic_app/settings/Profile.html', {})


def Video_repository(request):
    return render(request, 'basic_app/settings/Profile/Video_repository.html', {})


def Daliy_Tip(request):
    return render(request, 'basic_app/Menu/Chat/Daliy_Tip.html', {})


def Review(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            user = form.save()
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "basic_app/settings/Review.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
