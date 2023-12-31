# Generated by Django 4.2.3 on 2023-07-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aluguel", "0003_rent_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rent",
            name="address",
        ),
        migrations.AddField(
            model_name="rent",
            name="city",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AddField(
            model_name="rent",
            name="complement",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="rent",
            name="district",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AddField(
            model_name="rent",
            name="number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="rent",
            name="state",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="rent",
            name="street",
            field=models.CharField(default="", max_length=60),
        ),
        migrations.DeleteModel(
            name="Address",
        ),
    ]
