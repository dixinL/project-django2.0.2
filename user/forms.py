from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=20)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


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

