# Generated by Django 5.0 on 2024-03-02 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0020_galleries'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleries',
            name='title',
            field=models.CharField(default=1, max_length=88),
            preserve_default=False,
        ),
    ]