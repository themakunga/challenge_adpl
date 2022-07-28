from django.db import models
from area.models import Area
from user.models import User
class Mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    areas = models.ManyToManyField(Area)
    is_authorized = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
