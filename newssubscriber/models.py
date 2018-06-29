from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from django.urls import reverse

class Newsletter(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=100, primary_key=True)

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Relation(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='subscribers')
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name='newsletters')
    active = models.BooleanField(default=False, editable=False)
    token = models.CharField(max_length=40, default=get_random_string(40), editable=False)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return self.newsletter.name + ' <--> ' + self.subscriber.email

    def activate_url(self):
        return reverse('newssubscriber:token', kwargs={'action': 'activate', 'token': self.token})

    def delete_url(self):
        return reverse('newssubscriber:token', kwargs={'action': 'delete', 'token': self.token})

    def send_active_email(self):
        print(self.activate_url())
