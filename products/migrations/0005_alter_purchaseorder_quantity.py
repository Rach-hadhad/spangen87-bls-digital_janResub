# Generated by Django 3.2.16 on 2023-01-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_purchaseorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
