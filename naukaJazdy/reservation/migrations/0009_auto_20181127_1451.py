# Generated by Django 2.1.2 on 2018-11-27 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_auto_20181127_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='surname',
        ),
    ]
