from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(models.Model):
    child_age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userinfo')
