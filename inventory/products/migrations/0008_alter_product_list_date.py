# Generated by Django 4.0.1 on 2022-01-18 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 18, 15, 30, 57, 222850, tzinfo=utc)),
        ),
    ]