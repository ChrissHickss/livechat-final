from rest_framework.serializers import ModelSerializer, StringRelatedField
from social_django.models import UserSocialAuth
from .models import User


class UserListSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'first_name', 'email', 'phone_number']
 

class SocialListSerializer(ModelSerializer):
  user = UserListSerializer(many=False)

  class Meta:
    model = UserSocialAuth
    fields = '__all__'