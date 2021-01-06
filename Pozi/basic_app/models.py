from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

# Create your models here.
# from .forms import UserForm



class itemReviewToAdmin(models.Model):
    from_email = models.EmailField(null=True)
    subject = models.CharField(max_length=30)
    text = models.TextField(max_length=1000, null=True)

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


