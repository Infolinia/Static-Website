# Generated by Django 2.1.2 on 2018-10-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_remove_reservation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.CharField(choices=[('08:00:00', '08:00'), ('10:00:00', '10:00'), ('12:00:00', '12:00'), ('14:00:00', '14:00'), ('16:00:00', '16:00')], default='08:00', max_length=10),
        ),
    ]