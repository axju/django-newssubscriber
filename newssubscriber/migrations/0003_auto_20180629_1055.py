# Generated by Django 2.0.6 on 2018-06-29 08:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newssubscriber', '0002_auto_20180629_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relation',
            options={'ordering': ['-create_at']},
        ),
        migrations.AddField(
            model_name='relation',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='relation',
            name='active',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='relation',
            name='token',
            field=models.CharField(default='VipYX8rhThL2TeBtQCGQGkpswFIg1IPi4gzgCQHZ', editable=False, max_length=40),
        ),
    ]
