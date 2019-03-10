from django import forms
from django.contrib.auth.models import User
from WeGame.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.passwordInput())

    class Meta:
        model = User 
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    dateOfBirth = forms.DateField()
    class Meta:
        model = UserProfile
        fields = ('dateOfBirth')