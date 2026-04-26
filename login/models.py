from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EEducateAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(maxLength=20, unique=True)
    authorized_apps = models.JSONField(default=list)
    def __str__(self):
        return self.user.username
    