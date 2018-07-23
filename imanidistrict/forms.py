from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ('profile_image', 'phone_number', 'description')


class UserProfileChangeForm(UserCreationForm):

    class Meta(UserChangeForm.Meta):
        model = UserProfile
        fields = ('profile_image', 'phone_number', 'description')
