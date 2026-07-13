from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm, ProfileForm, PostForm
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
            return redirect("login-user")
        login(request=request, user=user)
        if request.user.profile is None:
            return redirect("profile")
        return redirect("home")
    return render(request, "login.html", {"form": form})


@login_required
def logout_user(request):
    logout(request=request)
    messages.success(request=request, message="Logout Succesfull")
    return redirect("login-user")


@login_required
def home(request):
    posts = Post.objects.all()
    form = PostForm()
    return render(
        request=request,
        template_name="index.html",
        context={"posts": posts, "form": form},
    )


@login_required
def profile(request):
    instance = Profile.objects.filter(user=request.user).first()
    form = ProfileForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        form.save()
        messages.success(request, message="Profile saved")
        return redirect(f"/profile/{request.user.username}")
    return render(request, "profileform.html", {"form": form})


@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, message="Post created")
    return redirect("/")


@login_required
def like_post(request, id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=id)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return redirect(f"/#post-{id}")


@login_required
def follow_profile(request, username):
    if request.method == "POST":
        target_profile = get_object_or_404(Profile, user__username=username)
        current_profile = request.user.profile
        if current_profile.following.filter(id=target_profile.id).exists():
            current_profile.following.remove(target_profile)
        else:
            current_profile.following.add(target_profile)
    return redirect(f"/profile/{username}")


@login_required
def user_profile(request, username):
    profile = Profile.objects.get(user__username=username)
    posts = Post.objects.filter(user__username=username)

    return render(
        request,
        "user-profile.html",
        {
            "profile": profile,
            "posts": posts,
            "is_myprofile": request.user.username == username,
        },
    )
