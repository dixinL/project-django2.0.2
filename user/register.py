from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("/")
        else:
            return render(request, "user/register.html", {
                'form': form,
            })
    else:
        form = RegisterForm()
        return render(request, "user/register.html", {
            'form': form,
        })