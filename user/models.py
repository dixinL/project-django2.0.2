from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


# 用户详细信息模型
class UserInfo(models.Model):
    child_age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')


