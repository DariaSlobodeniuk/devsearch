# Generated by Django 3.2.7 on 2021-09-20 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_review_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_total', '-vote_ratio', 'title']},
        ),
    ]
