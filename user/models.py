from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from expertise.models import Expertise
class User(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=200, null=True)
    employer = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    expertise = models.ManyToManyField(Expertise)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.last_name +' '+ self.first_name
