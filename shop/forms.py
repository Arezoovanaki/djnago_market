from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nam khod ra vared konid'})
        )
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nam khanevadegi khod ra vared konid'})
        )
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email khod ra vared konid'})
        )
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username khod ra vared konid','autocomplete': 'off'})
        )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
           attrs={
               'class':'form-control',
               'name': 'password',
               'type': 'password',
               'placeholder':'ramz khod ra vared konid'
           }
        )
        )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
           attrs={
               'class':'form-control',
               'name': 'password',
               'type': 'password',
               'placeholder':'ramz khod ra dobare vared konid'
           }
        )

    )
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email','username','password1','password2' 