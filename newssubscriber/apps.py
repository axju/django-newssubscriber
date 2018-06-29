from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.apps import apps as global_apps

class NewssubscriberConfig(AppConfig):
    name = 'newssubscriber'
    verbose_name = _('Newsletters')

    def ready(self):
        '''If there is no newsletter, create a default'''
        Newsletter = global_apps.get_model('newssubscriber', 'Newsletter')
        if Newsletter.objects.count() == 0:
            Newsletter(name='default').save()
