from rest_framework import serializers
from .models import Event, Subscription

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'sport', 'date', 'location', 'day_or_night', 'team', 'opponent', 'details')
        model = Event

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['user', 'event', 'text_notification']

