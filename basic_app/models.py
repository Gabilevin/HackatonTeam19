from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)


class NewReviewToAdmin(models.Model):
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text


class itemReviewToAdmin(models.Model):
    new_review = models.ForeignKey(NewReviewToAdmin, on_delete=models.CASCADE)
    subject = models.CharField(max_length=300)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
