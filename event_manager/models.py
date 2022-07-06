from django.db import models
from accounts.models import User

# Create your models here.
class Event(models.Model):
    user = models.ManyToManyField(User, through='Subscription')
    sport = models.CharField(max_length=255)
    date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    day_or_night = models.CharField(max_length=255, null=True, blank=True)
    team = models.CharField(max_length=255, null=True, blank=True)
    opponent = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.team} vs {self.opponent} - {self.date}'

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text_notification = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name
