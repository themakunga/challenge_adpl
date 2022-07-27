from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=200, null=True)
    employer = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    expertise = ArrayField(models.CharField(max_length=200, null=True), null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

