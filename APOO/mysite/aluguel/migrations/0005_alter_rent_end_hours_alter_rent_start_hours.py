# Generated by Django 4.2.3 on 2023-07-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aluguel", "0004_remove_rent_address_rent_city_rent_complement_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rent",
            name="end_hours",
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="rent",
            name="start_hours",
            field=models.TimeField(auto_now=True),
        ),
    ]
