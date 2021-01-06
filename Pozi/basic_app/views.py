from pyexpat.errors import messages

from accounts.form import register_extra
from django import template

from django.contrib.auth.models import User, Group
from django.core.mail import EmailMessage

from . import forms
from .models import stories_model
from .forms import ContactForm, stories_form
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from accounts.decorators import allowed_users
from django.template import RequestContext, loader


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


def index(request):
    query = request.GET.get("title")
    all_stories = None
    if query:
        all_stories = stories_model.objects.filter(subject__icontains=query)
    else:
        all_stories = stories_model.objects.all()
    context = {
        "stories": all_stories
    }
    return render(request, 'basic_app/index.html', context)


def consultation(request):
    return render(request, 'basic_app/Menu/consultation.html', {})


def stories(request):
    form = stories_form()
    if request.method == 'POST':
        form = stories_form(request.POST)

        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            form.save(commit=True)
        else:
            print('EROOR FORM INVALID')
        return redirect("basic_app:index")
    return render(request, 'basic_app/Menu/stories.html', {'form': form})


def font_changing(request):
    return render(request, 'basic_app/settings/font_changing.html', {})


def Videos(request):
    return render(request, 'basic_app/Menu/Videos.html', {})


def about(request):
    return render(request, 'basic_app/settings/about.html', {})


# def Profile(request):
#     return render(request, 'basic_app/settings/Profile.html', {})


def Video_repository(request):
    return render(request, 'basic_app/settings/Profile/Video_repository.html', {})


def Review(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            form.save(commit=True)

        else:
            print('EROOR FORM INVALID')
        return redirect("basic_app:index")

    return render(request, "basic_app/settings/Review.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user': user_list}
    return render(request, 'basic_app/users.html', context=user_dict)


def form_name_vew(request):
    form = forms.FormName()
    return render(request, 'basic_app/form_page.')


def detail(request, id):
    storie = stories_model.objects.get(id=id)

    context = {
        "story": storie
    }
    return render(request, 'basic_app/Menu/stories/detail.html', context)


def edit_story(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            story = stories_model.objects.get(id=id)

            if request.method == "POST":
                form = stories_form(request.POST, instance=story)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("basic_app:detail", id)
            else:
                form = stories_form(instance=story)
            return render(request, 'basic_app/Menu/stories.html', {"form": form}, )
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def delete_story(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            story = stories_model.objects.get(id=id)

            story.delete()
            return redirect("basic_app:stories")
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


@allowed_users(allowed_roles=['Admin'])
def login_report(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'basic_app/Managers/Login_Temporary_Report.html')
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


@allowed_users(allowed_roles=['Admin'])
def Consumption_report(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'basic_app/Managers/Content_Consumption_Report.html')
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


@allowed_users(allowed_roles=['Admin'])
def Recent_changes(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'basic_app/Managers/Recent_changes.html')
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def profile(request, id):
    user1 = User.objects.get(id=id)

    regiter_extra_model = request.user.regiter_extra_model
    form = register_extra(instance=regiter_extra_model)

    if request.method == 'POST':
        form = register_extra(request.POST, request.FILES, instance=regiter_extra_model)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'user1': user1,

    }
    return render(request, 'basic_app/settings/Profile/Profile.html', context)
