# Generated by Django 3.2.7 on 2021-09-10 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210909_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
