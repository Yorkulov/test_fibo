from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser

from test_project import settings


class CustomUser(AbstractUser):
    profile_picture = models.ImageField()
    groups_custom = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions_custom = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)


class MessageModel(models.Model):
    text = models.TextField()
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
