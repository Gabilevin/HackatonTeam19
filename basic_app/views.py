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

from django.shortcuts import render, redirect
from accounts.decorators import allowed_users
from django.template import RequestContext, loader


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
    user = User.objects.all()

    context = {
        "user": user
    }
    return render(request, 'basic_app/Menu/consultation.html', context)


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
