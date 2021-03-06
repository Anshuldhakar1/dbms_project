# Generated by Django 3.0.8 on 2020-07-15 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20200715_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Bidding',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BID', to=settings.AUTH_USER_MODEL),
        ),
    ]
