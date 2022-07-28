from django.db import models

# Create your models here.
class Expertise(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
