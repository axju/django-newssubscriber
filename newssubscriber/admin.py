from django.contrib import admin
from django.utils.translation import ugettext as _

from newssubscriber.models import Newsletter, Subscriber, Relation

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin_subscribers')

    def admin_subscribers(self, obj):
        return obj.subscribers.all().count()
    admin_subscribers.short_description = _('subscribers')

class RelationAdmin(admin.ModelAdmin):
    list_display = ('create_at', 'newsletter', 'subscriber', 'active', 'activate_url', 'token')


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscriber)
admin.site.register(Relation, RelationAdmin)
