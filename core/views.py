from django.shortcuts import render, redirect
from .models import Post, Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_user(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        exist = User.objects.filter(username=username).exists()
        if exist:
            messages.warning(
                request=request, message="Already registered user, please try login"
            )
            return redirect("/login")
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request=request, message="registration successfull")
        return redirect("/login")
    return render(request, "registration.html", {"form": form})


def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request=request, username=username, password=password)
        if not user:
            messages.error(request=request, message="Invalid username or password")
            return redirect("/login")
        login(request=request, user=user)
        return redirect("/profile")
    return render(request, "login.html", {"form": form})


def logout_user(request):
    logout(request=request)
    messages.success(request=request, message="Logout Succesfull")
    return redirect("/login")


def home(request):
    posts = Post.objects.all()
    return render(request=request, template_name="index.html", context={"posts": posts})


@login_required
def profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        form.save()
        messages.success(request, message="created profile")
        return redirect("/")
    return render(request, "profileform.html", {"form": form})
