from django.urls import path, include
from .views import *

urlpatterns = [
    #authorization links
    path('auth/', include('dj_rest_auth.urls')),    
    path('auth/register/', include('dj_rest_auth.registration.urls')),

    #views links
    path('users/', UserListView.as_view(), name='user_list'),
    path('social/', SocialListView.as_view(), name='social_user_list'),
    path('', index, name='home'),
    path('logout/', logout, name='logout'),
]
