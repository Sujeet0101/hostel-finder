# Generated by Django 4.1.6 on 2023-03-07 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_booking_options_booking_booker_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booker_email',
        ),
    ]