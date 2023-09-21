from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    pic = models.ImageField(upload_to='media/', default='media/no-profile-picture-4-1024x1024.jpg')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Tweets(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='media/', default='')
    likes = models.JSONField(default=None)
    retweets = models.JSONField(default=None)
    comments = models.JSONField(default=None)
    views = models.JSONField(default=None)
    date_time = models.DateTimeField(auto_now_add=True)

