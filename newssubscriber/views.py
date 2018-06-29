from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.contrib import messages

from newssubscriber.forms import SubscribeForm
from newssubscriber.models import Newsletter, Subscriber, Relation

import logging
logger = logging.getLogger('newssubscriber')

class SubscribeView(FormView):
    template_name = 'newssubscriber/subscribe.html'
    form_class = SubscribeForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        name = self.kwargs.get('newsletter', 'default')
        newsletter = Newsletter.objects.filter(name=name).first()

        if not newsletter:
            #fehler benden
            logger.error('The newsletter does not exist.')
            return super().form_valid(form)

        subscriber, created = Subscriber.objects.get_or_create(email=email)
        if created: logger.info('A new subscriber')

        relation, created = Relation.objects.get_or_create(subscriber=subscriber, newsletter=newsletter)

        mail_subject = 'MAIL_SUBJECT'
        message = 'http://' + get_current_site(self.request).domain + relation.activate_url()
        mail = EmailMessage(mail_subject, message, to=[email])
        mail.send()

        return super().form_valid(form)

class TokenActioneView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        relation = get_object_or_404(Relation, token=kwargs['token'])
        if kwargs['action'] == 'activate':
            relation.active = True
            relation.save()
            messages.success(self.request, 'Profile details updated.')
            logger.info('Subscriber activate')

        if kwargs['action'] == 'delete':
            relation.delete()
            logger.info('Subscriber delete')

        #article.update_counter()
        return super().get_redirect_url(*args, **kwargs)
