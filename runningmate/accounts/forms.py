from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import UserProfile


class SignupForm(forms.Form):
    class Meta:
        model = User

    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':''}),label="이름")
    school = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':'ex)동국대학교'}),label="학교")
    school_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'ex)2018111***'}), label="학번")


    def signup(self, request, user):
        userProfile = UserProfile()
        userProfile.user = user
        userProfile.name = self.cleaned_data[('name')]
        userProfile.email = user.email
        userProfile.school = self.cleaned_data[('school')]
        userProfile.school_id = self.cleaned_data[('school_id')]
        userProfile.save()
        user.save()
        return user