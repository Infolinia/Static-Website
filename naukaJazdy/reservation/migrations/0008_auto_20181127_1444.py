# Generated by Django 2.1.2 on 2018-11-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_reservation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='category',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('D', 'D'), ('T', 'T')], default='A', max_length=10, verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.TextField(verbose_name='Informacja do instruktora'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='surname',
            field=models.TextField(verbose_name='Informacja do instruktora'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(choices=[('08:00:00', '08:00'), ('10:00:00', '10:00'), ('12:00:00', '12:00'), ('14:00:00', '14:00'), ('16:00:00', '16:00')], default='08:00', max_length=10, verbose_name='Godzina'),
        ),
    ]