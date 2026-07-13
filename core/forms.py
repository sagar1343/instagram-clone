from django import forms
from .models import Profile, Post


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, widget=forms.TextInput({"class": "input"}))
    password = forms.CharField(
        widget=forms.PasswordInput({"type": "password", "class": "input"})
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=3, widget=forms.TextInput({"class": "input border-2"})
    )
    email = forms.EmailField(widget=forms.EmailInput({"class": "input"}))
    password = forms.CharField(
        widget=forms.PasswordInput({"type": "password", "class": "input"})
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "avatar", "birth_date"]
        widgets = {
            "bio": forms.TextInput({"class": "input"}),
            "avatar": forms.FileInput({"class": "file-input"}),
            "birth_date": forms.DateInput({"class": "input", "type": "date"}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "attachment"]
        widgets = {
            "caption": forms.TextInput(
                {
                    "class": "pl-8 input input-lg rounded-full grow",
                    "placeholder": "Write something in your mind...",
                }
            ),
            "attachment": forms.FileInput(
                {"class": "hidden", "id": "attachment-input"}
            ),
        }
