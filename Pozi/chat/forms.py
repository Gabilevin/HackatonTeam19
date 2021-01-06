from chat.models import chat_first_question_model, payment, tip_model, QA_model
from django import forms

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


class payment_form(forms.ModelForm):
    class Meta:
        model = payment
        fields = '__all__'
        exclude = 'user', 'aproved','date'


class tip_form(forms.ModelForm):
    class Meta:
        model = tip_model
        fields = ('subject', 'text',)


class QA_form(forms.ModelForm):
    class Meta:
        model = QA_model
        fields = ('subject', 'text',)
