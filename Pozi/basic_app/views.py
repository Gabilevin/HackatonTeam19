from pyexpat.errors import messages

from accounts.form import register_extra

from django.contrib.auth.models import User
from . import forms
from .models import stories_model, motivation, stand_up, sport, tip_model, QA_model
from .forms import ContactForm, stories_form, tip_form, QA_form, stand_up_form, sport_form, motivation_form, \
    chat_first_question_form
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from accounts.decorators import allowed_users
import random







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
    items = tip_model.objects.all()

    # if you want only a single random item
    random_item = random.choice(items)
    all_stories = None
    if query:
        all_stories = stories_model.objects.filter(subject__icontains=query)
    else:
        all_stories = stories_model.objects.all()
    context = {
        "stories": all_stories,
        "popup": random_item.text
    }
    return render(request, 'basic_app/index.html', context)


def consultation(request):
    return render(request, 'basic_app/Menu/consultation.html', {})


def cost_chat(request):
    return render(request, 'basic_app/Menu/Chat/cost_chat.html', {})


def free_chat(request):
    return render(request, 'basic_app/Menu/Chat/free_chat.html', {})


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


def video_stand_up(request):
    obj = stand_up.objects.all()

    return render(request, 'basic_app/Menu/videos/stand_up_comedy.html', {'obj': obj})


def add_stand_up_video(request):
    form = stand_up_form
    if request.method == 'POST':
        form = stand_up_form(request.POST)

        if form.is_valid():
            video = form.cleaned_data['video']

            form.save(commit=True)
        else:
            print('EROOR FORM INVALID')
            # return render(request, 'basic_app/index.html', {"error": "EROOR FORM INVALID."})
        return redirect("basic_app:stand_up_comedy")
    return render(request, 'basic_app/Menu/videos/stand_up/add_video_stand_up.html', {'form': form})


def stand_up_detail(request, id):
    All_video = stand_up.objects.get(id=id)

    context = {
        "stand_up_video": All_video
    }
    return render(request, 'basic_app/Menu/videos/stand_up/detail_stand_up.html', context)


def edit_stand_up(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            video = stand_up.objects.get(id=id)

            if request.method == "POST":
                form = stand_up_form(request.POST, instance=video)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("basic_app:stand_up_detail", id)
            else:
                form = stand_up_form(instance=video)
            return render(request, 'basic_app/Menu/videos/stand_up/add_video_stand_up.html', {"form": form}, )
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def delete_stand_up(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            video = stand_up.objects.get(id=id)

            video.delete()
            return redirect("basic_app:stand_up_comedy")
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def video_motivation(request):
    obj = motivation.objects.all()
    return render(request, 'basic_app/Menu/videos/motivation.html', {'obj': obj})


def add_motivation_video(request):
    form = motivation_form()
    if request.method == 'POST':
        form = motivation_form(request.POST)

        if form.is_valid():
            video = form.cleaned_data['video']

            form.save(commit=True)
        else:
            print('EROOR FORM INVALID')
            # return render(request, 'basic_app/index.html', {"error": "EROOR FORM INVALID."})
        return redirect("basic_app:motivation")
    return render(request, 'basic_app/Menu/videos/motivation/add_video_motivation.html', {'form': form})


def motivation_detail(request, id):
    All_video = motivation.objects.get(id=id)

    context = {
        "motivation_video": All_video
    }
    return render(request, 'basic_app/Menu/videos/motivation/detail_motivation.html', context)


def edit_motivation(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            video = motivation.objects.get(id=id)

            if request.method == "POST":
                form = motivation_form(request.POST, instance=video)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("basic_app:motivation_detail", id)
            else:
                form = motivation_form(instance=video)
            return render(request, 'basic_app/Menu/videos/motivation/add_video_motivation.html', {"form": form}, )
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def delete_motivation(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            video = motivation.objects.get(id=id)

            video.delete()
            return redirect("basic_app:motivation")
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def video_Sport(request):
    obj = sport.objects.all()
    return render(request, 'basic_app/Menu/videos/Sport.html', {'obj': obj})


def add_sport_video(request):
    form = sport_form()
    if request.method == 'POST':
        form = sport_form(request.POST)

        if form.is_valid():
            video = form.cleaned_data['video']

            form.save(commit=True)
        else:
            print('EROOR FORM INVALID')
            # return render(request, 'basic_app/index.html', {"error": "EROOR FORM INVALID."})
        return redirect("basic_app:Sport")
    return render(request, 'basic_app/Menu/videos/sport/add_video_sport.html', {'form': form})


def sport_detail(request, id):
    All_video = sport.objects.get(id=id)

    context = {
        "sport_video": All_video
    }
    return render(request, 'basic_app/Menu/videos/sport/detail_sport.html', context)


def edit_sport(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            video = sport.objects.get(id=id)

            if request.method == "POST":
                form = sport_form(request.POST, instance=video)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("basic_app:sport_detail", id)
            else:
                form = stand_up_form(instance=video)
            return render(request, 'basic_app/Menu/videos/sport/add_video_sport.html', {"form": form}, )
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def delete_sport(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            video = sport.objects.get(id=id)

            video.delete()
            return redirect("basic_app:sport")
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def about(request):
    return render(request, 'basic_app/settings/about.html', {})


# def Profile(request):
#     return render(request, 'basic_app/settings/Profile.html', {})


def Video_repository(request):
    return render(request, 'basic_app/settings/Profile/Video_repository.html', {})


def Daliy_Tip(request):
    All_Tips = tip_model.objects.all()
    context = {
        "Daliy_Tips": All_Tips
    }
    return render(request, 'basic_app/Menu/Chat/Daliy_Tip.html', context)


def tip_detail(request, id):
    All_Tips = tip_model.objects.get(id=id)

    context = {
        "Daliy_Tips": All_Tips
    }
    return render(request, 'basic_app/Menu/Chat/daliy_tip/tip_detail.html', context)


@allowed_users(allowed_roles=['Admin', 'Doc'])
def Daliy_Tip_add(request):
    form = tip_form()
    if request.method == 'POST':
        form = tip_form(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            form.save(commit=True)
            messages.success(request, 'Tip was created !')
        else:
            print('EROOR FORM INVALID')
            messages.error(request, 'Tip was not created !')
        return redirect("basic_app:Daliy_Tip")
    return render(request, 'basic_app/Menu/Chat/Daliy_Tip/add_Tip.html', {'form': form})


@allowed_users(allowed_roles=['Admin', 'Doc'])
def edit_tip(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            tip = tip_model.objects.get(id=id)

            if request.method == "POST":
                form = tip_form(request.POST, instance=tip)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("basic_app:tip_detail", id)
            else:
                form = tip_form(instance=tip)
            return render(request, 'basic_app/Menu/Chat/Daliy_Tip/add_Tip.html', {"form": form}, )
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


@allowed_users(allowed_roles=['Admin', 'Doc'])
def delete_tip(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            daliy_tip = tip_model.objects.get(id=id)

            daliy_tip.delete()
            return redirect("basic_app:Daliy_Tip")
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def QA(request):
    All_QA = QA_model.objects.all()
    context = {
        "QA": All_QA
    }
    return render(request, 'basic_app/Menu/Chat/QA.html', context)


def QA_detail(request, id):
    All_QA = QA_model.objects.get(id=id)

    context = {
        "QA": All_QA
    }
    return render(request, 'basic_app/Menu/Chat/QA/QA_detail.html', context)


@allowed_users(allowed_roles=['Admin', 'Doc'])
def QA_add(request):
    form = QA_form()
    if request.method == 'POST':
        form = QA_form(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            form.save(commit=True)
            messages.success(request, 'QA was created !')
        else:
            print('EROOR FORM INVALID')
            messages.error(request, 'QA was not created !')

        return redirect("basic_app:QA")
    return render(request, 'basic_app/Menu/Chat/QA/add_QA.html', {'form': form}, )


@allowed_users(allowed_roles=['Admin', 'Doc'])
def edit_QA(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            QA = QA_model.objects.get(id=id)

            if request.method == "POST":
                form = QA_form(request.POST, instance=QA)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("basic_app:QA_detail", id)
            else:
                form = QA_form(instance=QA)
            return render(request, 'basic_app/Menu/Chat/QA/add_QA.html', {"form": form}, )
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


@allowed_users(allowed_roles=['Admin', 'Doc'])
def delete_QA(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            QA = QA_model.objects.get(id=id)

            QA.delete()
            return redirect("basic_app:QA")
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


def Review(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            release_date = form.cleaned_data['release_date']
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





def Expert_questions(request):
    form = chat_first_question_form()
    if request.method == "POST":
        form = chat_first_question_form(request.POST or None)

        if form.is_valid():
            user3 = request.user
            form.instance.user = user3
            form.save()
        else:
            print('EROOR FORM INVALID')
        return redirect("basic_app:cost_chat")

    return render(request, 'basic_app/Menu/Chat/cost_chat/expert_questions.html', {'form': form})


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
