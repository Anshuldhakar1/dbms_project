# Generated by Django 3.0.8 on 2020-07-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='Time',
            field=models.TimeField(null=True),
        ),
    ]
