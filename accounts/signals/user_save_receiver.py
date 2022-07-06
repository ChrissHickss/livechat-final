# Django Signal
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User

# Google API
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'accounts/signals/credentials.json'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

@receiver(post_save, sender=User)
def user_save_receiver(sender, created, instance, **kwargs):
  if instance.calendar_id == None:
    # Call Google API - Create New Calendar for user
    instance.calendar_id = create_calendar()
    instance.save()
    print("Added calendar_id to user")

def create_calendar():
  try:
    service = build('calendar', 'v3', credentials=credentials)
    calendar = {
      "summary": "AOTG Calendar",
      "timeZone": "America/New_York"
    }
    created_calendar = service.calendars().insert(body=calendar).execute()
    print(created_calendar["id"])
    return created_calendar["id"]

  except HttpError as error:
      print('An error occurred: %s' % error)
