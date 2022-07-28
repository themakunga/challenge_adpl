from django.db import models
from mentor.models import Mentor

class Availability(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
