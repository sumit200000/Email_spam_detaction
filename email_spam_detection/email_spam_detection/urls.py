# email_spam_detection/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spam_detection.urls')),  # Include app URLs
]
