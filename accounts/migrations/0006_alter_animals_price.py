# Generated by Django 5.0.7 on 2025-04-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_remove_animals_imageurl_animals_imagefile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animals",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
