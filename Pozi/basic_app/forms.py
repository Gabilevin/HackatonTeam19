from django.contrib.auth.models import User
from django.db.models import Q, __all__
from django.forms import models
from quorum.exceptions import ValidationError
from django.core import validators
from django import forms

from basic_app.models import itemReviewToAdmin, stories_model, tip_model, QA_model, stand_up, sport, motivation, \
    chat_first_question_model

YEARS = [x for x in range(1940, 2021)]


class UserForm_Date(forms.Form):
    birth_date = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget(years=YEARS))


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    gender = (('male', "Male"), ('female', "Famale"))
    Gender = forms.ChoiceField(choices=gender)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ContactForm(forms.ModelForm):
    class Meta():
        model = itemReviewToAdmin
        fields = '__all__'


class stories_form(forms.ModelForm):
    class Meta():
        model = stories_model
        exclude = 'release_date',


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


class storieform(forms.ModelForm):
    class Meta:
        model = stories_model
        fields = ('subject', 'text')


class tip_form(forms.ModelForm):
    class Meta:
        model = tip_model
        fields = ('subject', 'text', )


class QA_form(forms.ModelForm):
    class Meta:
        model = QA_model
        fields = ('subject', 'text', )


class stand_up_form(forms.ModelForm):
    class Meta:
        model = stand_up
        fields = ('video',)


class sport_form(forms.ModelForm):
    class Meta:
        model = sport
        fields = ('video',)


class motivation_form(forms.ModelForm):
    class Meta:
        model = motivation
        fields = ('video',)


feel_today = (('good', "GOOD"), ('bad', "Bad"), ('excellent', "Excellent"), ('okay', "Okay"))


class chat_first_question_form(forms.ModelForm):
    taking_medication = forms.CharField(widget=forms.Textarea)
    Medication_sensitivity = forms.CharField(widget=forms.Textarea)
    Corona_feeling = forms.CharField(widget=forms.Textarea)
    if_psychologist = forms.CharField(widget=forms.Textarea)
    about_yourself = forms.CharField(widget=forms.Textarea)
    feel = forms.ChoiceField(choices=feel_today)

    class Meta:
        model = chat_first_question_model
        fields = '__all__'
        exclude = 'user',
