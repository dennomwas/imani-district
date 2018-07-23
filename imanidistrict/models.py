import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(AbstractUser):
    profile_image = models.ImageField(upload_to='images', blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    description = models.TextField(
        max_length=200, help_text="Small Bio about yourself", blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.username


class Event(models.Model):
    """
    Model representing events for the district fellowship.
    """
    event_name = models.CharField(
        max_length=200, help_text="Enter the name of the Event")
    event_image = models.ImageField(upload_to='images', blank=True)
    event_description = models.TextField(
        max_length=1000, help_text="Enter the description of the Event")
    event_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    event_location = models.CharField(
        max_length=200, help_text="Enter the location of the Event")
    organized_by = models.ForeignKey(
        'UserProfile', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['event_date']

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.event_name


class SermonCategories(models.Model):

    category_name = models.CharField(
        max_length=50, help_text="Enter a Sermon Category")
    date_created = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.category_name


class Sermon(models.Model):

    sermon_title = models.CharField(
        max_length=200, help_text="Enter the name of the Sermon")
    sermon_image = models.ImageField(upload_to='images', blank=True)
    sermon_description = models.TextField(
        max_length=1000, help_text="Enter the description of the Event")
    sermon_date = models.DateField()

    sermon_by = models.ForeignKey(
        'UserProfile', on_delete=models.SET_NULL, null=True, related_name='sermons')

    sermon_category = models.ForeignKey(
        'SermonCategories', on_delete=models.SET_NULL, null=True, related_name='sermons')

    class Meta:
        ordering = ['sermon_date']

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.sermon_title
