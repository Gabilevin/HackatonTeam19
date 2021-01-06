from django.contrib.auth.models import User
from django.db.models import Q
from django.forms import models
from quorum.exceptions import ValidationError

from .models import UserProfileInfo

from django import forms

YEARS = [x for x in range(1940, 2021)]


class UserForm_Date(forms.Form):
    birth_date = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    gender = (('male', "Male"), ('female', "Famale"))
    Gender = forms.ChoiceField(choices=gender)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        exclude = 'profile_pic',


class ChangeEmailForm(forms.Form):
    email = forms.EmailField(label='Email')

    def init(self, user, *args, **kwargs):
        self.user = user
        super()._init_(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']

        if email == self.user.email:
            raise ValidationError(('Please enter another email.'))

        user = User.objects.filter(Q(email__iexact=email) & ~Q(id=self.user.id)).exists()
        if user:
            raise ValidationError(('You can not use this mail!!!!.',))

        return email


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)