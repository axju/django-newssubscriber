from django.urls import path

from newssubscriber.views import SubscribeView, TokenActioneView

app_name = 'newssubscriber'

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('<str:newsletter>/subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('<str:action>/<str:token>/', TokenActioneView.as_view(), name='token'),
]
