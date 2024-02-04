# Generated by Django 4.2.8 on 2024-02-04 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0066_servicelevel_carrier_service_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deutschepostsettings",
            name="customer_number",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
