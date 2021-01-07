from django.shortcuts import render, redirect

# Create your views here.
from .forms import stand_up_form, sport_form, motivation_form
from .models import motivation, stand_up, sport
from accounts.decorators import unatenticated_user, allowed_users


def video_stand_up(request):
    obj = stand_up.objects.all()

    return render(request, 'video/stand_up_comedy.html', {'obj': obj})


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
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
        return redirect("video:stand_up_comedy")
    return render(request, 'video/stand_up/add_video_stand_up.html', {'form': form})


def stand_up_detail(request, id):
    All_video = stand_up.objects.get(id=id)

    context = {
        "stand_up_video": All_video
    }
    return render(request, 'video/stand_up/detail_stand_up.html', context)


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def edit_stand_up(request, id):

            video = stand_up.objects.get(id=id)

            if request.method == "POST":
                form = stand_up_form(request.POST, instance=video)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("video:stand_up_detail", id)
            else:
                form = stand_up_form(instance=video)
            return render(request, 'video/stand_up/add_video_stand_up.html', {"form": form}, )



@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def delete_stand_up(request, id):

            video = stand_up.objects.get(id=id)

            video.delete()
            return redirect("video:stand_up_comedy")


def video_motivation(request):
    obj = motivation.objects.all()
    return render(request, 'video/motivation.html', {'obj': obj})


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
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
        return redirect("video:motivation")
    return render(request, 'video/motivation/add_video_motivation.html', {'form': form})


def motivation_detail(request, id):
    All_video = motivation.objects.get(id=id)

    context = {
        "motivation_video": All_video
    }
    return render(request, 'video/motivation/detail_motivation.html', context)


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def edit_motivation(request, id):

            video = motivation.objects.get(id=id)

            if request.method == "POST":
                form = motivation_form(request.POST, instance=video)

                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("video:motivation_detail", id)
            else:
                form = motivation_form(instance=video)
            return render(request, 'video/motivation/add_video_motivation.html', {"form": form}, )


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def delete_motivation(request, id):

            video = motivation.objects.get(id=id)

            video.delete()
            return redirect("video:motivation")



def video_Sport(request):
    obj = sport.objects.all()
    return render(request, 'video/Sport.html', {'obj': obj})


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
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
        return redirect("video:Sport")
    return render(request, 'video/sport/add_video_sport.html', {'form': form})


def sport_detail(request, id):
    All_video = sport.objects.get(id=id)

    context = {
        "sport_video": All_video
    }
    return render(request, 'video/sport/detail_sport.html', context)


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def edit_sport(request, id):
    video = sport.objects.get(id=id)

    if request.method == "POST":
        form = sport_form(request.POST, instance=video)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("video:sport_detail", id)
    else:
        form = stand_up_form(instance=video)
    return render(request, 'video/sport/add_video_sport.html', {"form": form}, )


@allowed_users(allowed_roles=['Admin', 'Doc', 'student_Doc'])
def delete_sport(request, id):
    video = sport.objects.get(id=id)

    video.delete()
    return redirect("video:Sport")
