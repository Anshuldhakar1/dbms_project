# Generated by Django 3.1.3 on 2021-06-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_auto_20210626_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Image',
            field=models.URLField(blank=True, max_length=400),
        ),
    ]
