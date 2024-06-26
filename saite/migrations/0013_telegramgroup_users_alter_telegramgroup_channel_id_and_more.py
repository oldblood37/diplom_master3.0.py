# Generated by Django 4.1.7 on 2024-05-28 20:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("saite", "0012_alter_telegramgroup_channel_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="telegramgroup",
            name="users",
            field=models.ManyToManyField(
                blank=True, related_name="telegram_groups", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="telegramgroup",
            name="channel_id",
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name="UserTelegramGroup",
        ),
    ]
