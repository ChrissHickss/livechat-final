from rest_framework import viewsets
from .serializers import EventSerializer, SubscriptionSerializer
from .models import Event, Subscription
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class EventView(viewsets.ModelViewSet):  
    serializer_class = EventSerializer   
    queryset = Event.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sport', 'date', 'location', 'day_or_night', 'team', 'opponent', 'details']

class SubscriptionView(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer   
    queryset = Subscription.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'event', 'text_notification']
