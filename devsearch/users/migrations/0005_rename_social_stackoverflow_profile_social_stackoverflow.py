# Generated by Django 3.2.7 on 2021-09-13 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_social_stackoverflow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_Stackoverflow',
            new_name='social_stackoverflow',
        ),
    ]
