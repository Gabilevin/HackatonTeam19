from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

# Create your models here.
# from .forms import UserForm

from django.db import models
from embed_video.fields import EmbedVideoField


class stand_up(models.Model):
    video = EmbedVideoField(blank=True)


class sport(models.Model):
    video = EmbedVideoField(blank=True)


class motivation(models.Model):
    video = EmbedVideoField(blank=True)


class itemReviewToAdmin(models.Model):
    from_email = models.EmailField(null=True)
    subject = models.CharField(max_length=30)
    text = models.TextField(max_length=1000, null=True)
    release_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.text


class stories_model(models.Model):
    from_email = models.EmailField(null=True)
    subject = models.CharField(max_length=300)
    text = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return self.subject

    def __unicode__(self):
        return self.subject


class tip_model(models.Model):
    subject = models.CharField(max_length=300)
    text = models.TextField(max_length=5000, null=True)
    release_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.subject

    def __unicode__(self):
        return self.subject


class QA_model(models.Model):
    subject = models.CharField(max_length=300)
    text = models.TextField(max_length=5000, null=True)
    release_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.subject

    def __unicode__(self):
        return self.subject


feel_today = (('good', "GOOD"), ('bad', "Bad"), ('excellent', "Excellent"), ('okay', "Okay"))


class chat_first_question_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    taking_medication = models.CharField(max_length=5000)
    Medication_sensitivity = models.CharField(max_length=5000)
    Corona_feeling = models.CharField(max_length=5000)
    if_psychologist = models.CharField(max_length=5000)
    about_yourself = models.CharField(max_length=5000)
    feel = models.CharField(max_length=9, choices=feel_today, null=True)

    def __str__(self):
        return str(self.user)
