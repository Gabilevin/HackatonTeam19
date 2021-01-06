from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import regiter_extra_model
from django.db.models import ImageField


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


YEARS = [x for x in range(1940, 2021)]


class UserForm_Date(forms.Form):
    birth_date = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))


gender = (('male', "Male"), ('female', "Famale"))


class register_extra(forms.ModelForm):
    Gender = forms.ChoiceField(choices=gender)
    class Meta:
        model = regiter_extra_model
        fields = ('image', 'date', 'Gender')
