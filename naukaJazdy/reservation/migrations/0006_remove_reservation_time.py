# Generated by Django 2.1.2 on 2018-10-25 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_auto_20181025_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='time',
        ),
    ]
