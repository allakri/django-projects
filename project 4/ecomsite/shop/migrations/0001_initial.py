# Generated by Django 5.1.4 on 2025-01-03 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("price", models.FloatField()),
                ("discount", models.FloatField()),
                ("category", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image", models.CharField(max_length=500)),
            ],
        ),
    ]