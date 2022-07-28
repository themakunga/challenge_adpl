from django.db import models

from user.models import User
from mentor.models import Mentor

class Reservation(models.Model):
    mentor = models.ManyToManyField(Mentor)
    user = models.ManyToManyField(User)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
