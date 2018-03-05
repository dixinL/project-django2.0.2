from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime
# Create your models here.


# 课程模型
# TODO：label
class CurriculumInfo(models.Model):
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='curriculum_info')
    file_name = models.CharField(max_length=50)
    path = models.FilePathField()
    series = models.CharField(verbose_name='系列', max_length=50)
    price = models.IntegerField(verbose_name='价格')
    grade = models.CharField(verbose_name='年级', max_length=50)


# class UploadForm(forms.ModelForm):
#     file = forms.FileField(label='请上传文件')
#
#     class Meta:
#         models = CurriculumInfo
#         field = ('series',)
#         exclude = ('path', 'date', 'owner', 'file_name', 'path',)

