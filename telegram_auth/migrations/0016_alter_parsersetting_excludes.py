# Generated by Django 4.1.7 on 2024-05-28 22:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("telegram_auth", "0015_alter_parsersetting_excludes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parsersetting",
            name="excludes",
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
