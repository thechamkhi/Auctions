# Generated by Django 4.2.5 on 2023-09-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing_alter_user_id_watchlist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='current_bid',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, null=True),
        ),
    ]