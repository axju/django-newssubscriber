from django.shortcuts import render
from django.views.generic.edit import FormView

from newssubscriber.forms import SubscribeForm

import logging
logger = logging.getLogger('newssubscriber')

class SubscribeView(FormView):
    template_name = 'newssubscriber/subscribe.html'
    form_class = SubscribeForm
    success_url = '/'

    def form_valid(self, form):
        logger.info('A new subscriber')

        #form.send_email()
        return super().form_valid(form)
