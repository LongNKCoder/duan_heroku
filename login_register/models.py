from django.db import models
from django.core.cache import cache 
import datetime
from chotot import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11,unique=True, blank=False)
    balance = models.IntegerField(default = 0)
    pic = models.ImageField(upload_to='pic', blank=False, default="pic/default.jpg")
    address = models.TextField(blank=True)
    def __str__(self):
        return self.user.username