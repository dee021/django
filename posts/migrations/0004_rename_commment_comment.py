# Generated by Django 3.2 on 2023-09-20 05:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('posts', '0003_commment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commment',
            new_name='Comment',
        ),
    ]
