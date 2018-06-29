from django.urls import path

from newssubscriber.views import SubscribeView

app_name = 'newssubscriber'

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]
