from django.urls import path, include
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path('o/', include(oauth2_urls, namespace='oauth2_provider')),
]
