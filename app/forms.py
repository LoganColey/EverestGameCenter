from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username...', 'style':'width: 300px; color: black;'}), max_length=20, required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Password...', 'style':'width: 300px; color: black;'}), max_length=15, required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username...', 'style':'width: 300px; color: black;'}), max_length=20, required=True)
    password1 = forms.CharField(label="Password", widget=forms.TextInput(attrs={'placeholder':'Password...', 'style':'width: 300px; color: black;'}), max_length=15, required=True)
    password2 = forms.CharField(label="Repeat Password", widget=forms.TextInput(attrs={'placeholder':'Repeat Password...', 'style':'width: 300px; color: black;'}), max_length=15, required=True)
    # class Meta:
    #     model = User
    #     fields = ['username', 'password1', 'password2']