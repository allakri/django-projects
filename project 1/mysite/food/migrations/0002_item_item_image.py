# Generated by Django 5.0.7 on 2024-12-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://cdn.vectorstock.com/i/500p/42/11/creative-concept-of-brain-food-symbolized-vector-53434211.jpg",
                max_length=500,
            ),
        ),
    ]
