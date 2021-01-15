from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm): #форма регистрации
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class LoginForm(forms.Form): #форма логина
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserEditForm(forms.ModelForm): #форма изменения юзера
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm): #форма изменения профиля юзера
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')