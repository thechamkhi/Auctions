# Generated by Django 4.2.5 on 2023-09-26 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_content_comment_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid_amount',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='bid',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='listing',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='won_listings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
