# Generated by Django 3.0.8 on 2020-07-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200715_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Bid',
            field=models.FloatField(null=True),
        ),
    ]
