from django.db import models
from django.contrib.auth.models import AbstractUser
# from social_django.models import UserSocialAuth

class User(AbstractUser):
    first_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    calendar_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name
