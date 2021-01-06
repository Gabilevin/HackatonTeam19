from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count
from datetime import datetime, timedelta

# Create your models here.

class regiter_extra_model(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/def.jpg',upload_to='profile_pics/', blank=True, null=True)
    date = models.DateField(null=True,blank=True)
    gender = (('male', "Male"), ('female', "Famale"))
    Gender = models.CharField(choices=gender, max_length=300,null=True)


    def __str__(self):
        return str(self.user)


class LoginDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=datetime.now(), blank=False)
