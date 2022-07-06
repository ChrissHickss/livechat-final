from django.contrib import admin
from django.urls import path, include
from rest_framework import routers              
from event_manager import views


router = routers.SimpleRouter()  
router.register(r'event', views.EventView)
router.register(r'subscription', views.SubscriptionView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('accounts.urls')),
    path('', include('accounts.urls')),
    path('events/', include(router.urls)),
    path('subscription/', include('event_manager.urls')),
    path('', include('social_django.urls')),
]
