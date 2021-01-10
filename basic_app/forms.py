
from django import forms

from basic_app.models import itemReviewToAdmin, stories_model

YEARS = [x for x in range(1940, 2021)]


class ContactForm(forms.ModelForm):
    class Meta():
        model = itemReviewToAdmin
        fields = '__all__'


class stories_form(forms.ModelForm):
    class Meta():
        model = stories_model
        exclude = 'release_date',





