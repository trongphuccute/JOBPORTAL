from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import logout


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('/')

    return render(request, "auth/register.html", {"form": form})


def user_login(request):
    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/')

    return render(request, "auth/login.html", {"form": form})
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('/login/')