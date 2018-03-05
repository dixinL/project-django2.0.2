from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import InfoFillForm
from .models import UserInfo


# 用户的个人信息展示界面
def user_info_view(request):
    context = {}
    user = User.objects.get(username=request.user.username)
    child = user.user_info.all().filter(user=user.id)
    context['child'] = []
    for i in range(len(child)):
        age = child[i].child_age
        context['child'].append(age)
    context['user'] = user.username

    return render(request, 'user/user_info.html', context)


# 用户的详细信息填写界面
def info_fill_view(request):
    if request.method == 'POST':
        form = InfoFillForm(request.POST)
        if form.is_valid():
            user = request.user
            info = UserInfo(child_age=form.cleaned_data['child_age'], user=user)
            info.save()
            return redirect('/')
        else:
            return redirect('info_fill')
    else:
        form = InfoFillForm()
        return render(request, 'user/info_fill.html', {'form':form})