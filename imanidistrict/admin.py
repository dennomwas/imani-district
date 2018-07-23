from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserProfileCreationForm, UserProfileChangeForm
from .models import Event, Sermon, UserProfile, SermonCategories


class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ['profile_image', 'phone_number', 'description', ]


admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(Sermon)
admin.site.register(SermonCategories)
