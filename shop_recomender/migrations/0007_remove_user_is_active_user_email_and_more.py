# Generated by Django 4.2.2 on 2023-07-14 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "shop_recomender",
            "0006_remove_user_email_remove_user_is_authenticated_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.AddField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_authenticated",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="Unknown", max_length=255),
        ),
        migrations.AddField(
            model_name="user",
            name="registration_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 14, 8, 6, 22, 283564, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
