from django.forms import ModelForm
from django import forms
from .models import Info, AdminLogin

class Infoform(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['username', 'password']
        username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Email address',
        'class': 'w-full py-4 px-6 rounded-xl'
        }))
        password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
        }))


class AdminLogin(forms.ModelForm):
    class Meta:
        model = AdminLogin
        fields = ['username', 'password']
        username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'
        }))
        password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
        }))