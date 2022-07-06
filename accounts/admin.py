from django.contrib import admin
from .models import User
# from social_django.models import UserSocialAuth
# from twilio.rest import Client
# from django.conf import settings
from .views import send_text, send_verification_text


# def send_text(modeladmin, request, queryset):
#   client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN )
#   for user in queryset:
#     message = client.messages.create(
#       to= str(user.phone_number), 
#       from_="+14123247978", # insert trial number 
#       body="Hey I hope you received this message") # insert message
# send_text.short_description = "Send text campaign"

class UserAdmin(admin.ModelAdmin):
  fields = ['first_name', 'phone_number']

  actions = [send_text, send_verification_text]



admin.site.register(User, UserAdmin)