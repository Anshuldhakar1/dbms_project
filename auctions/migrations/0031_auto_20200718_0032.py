# Generated by Django 3.0.8 on 2020-07-17 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_auto_20200717_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Bid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='auctions.Bid'),
        ),
    ]