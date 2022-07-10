from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    start_date = models.DateField(auto_created=True)
    end_date = models.DateField(auto_created=True)
    duration = models.DurationField()
    image = models.ImageField()  # pip install pillow package

class Tasks(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
