# Generated by Django 2.1.7 on 2019-03-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("accounts", "0026_auto_20190204_2042")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="deletion_notice_date",
            field=models.DateTimeField(blank=True, null=True),
        )
    ]
