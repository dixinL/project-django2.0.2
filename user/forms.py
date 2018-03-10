from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=20)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


# 普通用户注册表单
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=11, help_text='请输入您的11位手机号码')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

    def clean_username(self):
        username = self.cleaned_data['username']
        num_words = len(username)
        if num_words != 11 or not username.isdigit():
            raise forms.ValidationError("请输入正确的手机号码")
        return username


# 老师用户注册表单
class TeacherRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=11, help_text='请输入您的11位手机号码', label='用户名')
    id_card = forms.CharField(max_length=18, help_text='请输入您的18位身份证号码', label='身份证号码')
    real_name = forms.CharField(max_length=10, help_text='请输入您的真实姓名', label='真实姓名')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

    def clean_username(self):
        username = self.cleaned_data['username']
        num_words = len(username)
        if num_words != 11 or not username.isdigit():
            raise forms.ValidationError("请输入正确的手机号码")
        return username

    def clean_id_card(self):
        id_card = self.cleaned_data['id_card']
        num_words = len(id_card)
        if num_words != 18 or not id_card[0:17].isdigit():
            raise forms.ValidationError("请输入正确的身份证号码")
        return id_card


# 用户详细信息填写界面的表单
class InfoFillForm(forms.Form):
    child_age = forms.IntegerField(label='孩子的年龄')

