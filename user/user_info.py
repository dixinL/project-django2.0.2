from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# 用户的个人信息展示界面


def user_info_view(req):
    context = {}
    user = User.objects.get(username=req.session['username'])
    context['user'] = req.session['username']
    for child in user.children.all():
        child_name = child.children_name
        child_age = child.children_age
        context['child_age'] = child_age
        context['child_name'] = child_name
    return render(req, 'user_info.html', context)