# Generated by Django 1.11.6 on 2018-01-09 12:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("payments", "0003_subscription_address_id")]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="send_invoices",
            field=models.BooleanField(default=True),
        )
    ]
