# Generated by Django 2.1.5 on 2020-06-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_transfer_order_directionname'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer_order',
            name='fee',
            field=models.CharField(default=1, max_length=254),
        ),
    ]
