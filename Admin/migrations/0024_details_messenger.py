# Generated by Django 5.0.4 on 2024-05-14 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0023_countuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='messenger',
            field=models.CharField(max_length=1888, null=True),
        ),
    ]
