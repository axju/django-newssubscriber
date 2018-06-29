=====================
Django newssubscriber
=====================

!!!under develop!!!
-------------------

A small email basied newsletter. More information comming soon.

It will by push to https://pypi.org soon. And maybe I write some help for other
people.

Quick start
-----------

1. Add "newssubscriber" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'newssubscriber',
    ]

2. Include the newssubscriber URLconf in your project urls.py like this::

    path('newsletter/', include('newssubscriber.urls')),

3. Run `python manage.py migrate` to create the newssubscriber models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to configurat the newssubscriber (you'll need the Admin app enabled).
