# Generated by Django 5.0.3 on 2024-03-27 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhh', '0003_member_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='slug',
        ),
    ]
