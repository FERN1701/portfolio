# Generated by Django 5.0 on 2024-03-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_alter_details_details_photo1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='visibilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_youtube', models.IntegerField(default='0')),
                ('for_portfolio_profile', models.IntegerField(default='0')),
            ],
        ),
    ]
