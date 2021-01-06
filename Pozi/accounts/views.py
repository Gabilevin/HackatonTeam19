from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from basic_app.models import itemReviewToAdmin
from .form import RegistrationForm, register_extra
from .models import regiter_extra_model, User
from django.contrib.auth import authenticate, login, logout
from .decorators import unatenticated_user
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
from django.http import HttpResponse
from accounts.decorators import allowed_users
from django.db.models import Count

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from datetime import datetime

class UserListView(ListView):
    model = User

#Login_Temporary_Report

def user_render_pdf_view(request,*args,**kwargs):
    pass



def render_pdf_view(request):

    template_path = 'accounts/Managers/pdf1.html'
    user_list = User.objects.order_by('first_name')
    month = datetime.now().month
    #count = User.objects.filter(User.objects.date_joined.month == month).count()
    user_dict = {'user': user_list,'month':month}
        # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
            #Download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            #Dispaly
    response['Content-Disposition'] = 'filename="report.pdf"'
        # find the template and render it.
    template = get_template(template_path)
    html = template.render(user_dict)

        # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
        # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def render_pdf_login(request):
    day = datetime.now().day
    template_path = 'accounts/Managers/Content_Consumption_Report.html'
    reviews_list = itemReviewToAdmin.objects.order_by('id')
    reviews_dict = {'review': reviews_list,'day' : day}
        # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
            #Download
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            #Dispaly
    response['Content-Disposition'] = 'filename="report.pdf"'
        # find the template and render it.
    template = get_template(template_path)
    html = template.render(reviews_dict)

        # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
        # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response





@allowed_users(allowed_roles=['Admin'])
def login_report(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'accounts/Managers/Login_Temporary_Report.html')
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


@allowed_users(allowed_roles=['Admin'])
def Consumption_report(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'accounts/Managers/Content_Consumption_Report.html')
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")


@allowed_users(allowed_roles=['Admin'])
def Recent_changes(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'accounts/Managers/Recent_changes.html')
        else:
            return redirect("basic_app:index")

    return redirect("accounts:login")




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
                profile = form1.save(commit=False)
                profile.user = user

                if 'image' in request.FILES:
                    profile.image = request.FILES['image']
                profile.save()
                user1 = form1.save()

                user.is_active = False

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

                domain = get_current_site(request).domain
                link = reverse('accounts:activate',
                               kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})
                email_subject = 'Activate your account'
                activate_url = 'http//' + domain + link
                email_body = 'Hi ' + user.username + 'Please use this link to verfy your account/n' + activate_url

                email = EmailMessage(
                    email_subject,
                    email_body,
                    'rafulhelp@gmail.com',
                    [user.email],
                )

                email.send(fail_silently=False)

                group = Group.objects.get(name='customer')
                user.groups.add(group)
                return redirect("basic_app:index")
        else:
            form = RegistrationForm()
            form1 = register_extra()
        return render(request, "accounts/register.html", {"form": form, "form1": form1})


class VerificationView(View):
    def get(self, request, uidb64, token):
        return redirect('accounts:login')


@unatenticated_user
def login_user(request):
    if request.user.is_authenticated:
        return redirect("basic_app:index")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)


            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("basic_app:index")
                else:
                    return render(request, 'accounts/login.html', {"error": "your account has been disabled."})
            else:
                return render(request, 'accounts/login.html', {"error": "invalid Username or Password.try again."})
        return render(request, 'accounts/login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("accounts:login")
    else:
        return redirect("accounts:login")
