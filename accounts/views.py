from django.shortcuts import render, redirect
from .serializers import SocialListSerializer, UserListSerializer
from rest_framework import generics
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from .models import User
from twilio.rest import Client
from datetime import datetime, timedelta




class UserListView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserListSerializer

class SocialListView(generics.ListCreateAPIView):
  queryset = UserSocialAuth.objects.all()
  serializer_class = SocialListSerializer

def index(request):
  return render(request, 'index.html')

@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://localhost:8000' # this can be current domain
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')



# twilio stuff below here
def send_text(modeladmin, request, queryset):
  client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN )
  for user in queryset:
    message = client.messages.create(
      messaging_service_sid='MG13c314d08a8e8cf7546d50f81330acf0',
      body='This is a scheduled message',
      send_at=datetime.now() + timedelta(minutes = 16),
      schedule_type='fixed',
      to= str(user.phone_number), 
      from_="+14123247978", # insert trial number 
    )

send_text.short_description = "Schedule Text Campaign"


# Call this to get Verification Text:
def send_verification_text(modeladmin, request, queryset):
  client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN )
  for user in queryset:
    message = client.messages.create(
      to= str(user.phone_number), 
      from_="+14123247978", # insert trial number 
      body="This is your verification text. Thank you for subscribing to AOTG."
    )

send_verification_text.short_description = "Send verification text"