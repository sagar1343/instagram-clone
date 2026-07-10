from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, widget=forms.TextInput({"class": "input"}))
    password = forms.CharField(
        widget=forms.PasswordInput({"type": "password", "class": "input"})
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        min_length=10, widget=forms.TextInput({"class": "input border-2"})
    )
    email = forms.EmailField(widget=forms.EmailInput({"class": "input"}))
    password = forms.CharField(
        widget=forms.PasswordInput({"type": "password", "class": "input"})
    )


class ProfileForm(forms.Form):
    bio = forms.CharField(widget=forms.TextInput({"class": "input"}))
    avatar = forms.ImageField(
        widget=forms.FileInput({"class": "input", "type": "file", "accepts": ".jpg"})
    )
    birth_date = forms.DateField(
        widget=forms.DateInput({"class": "input", "type": "date"})
    )
