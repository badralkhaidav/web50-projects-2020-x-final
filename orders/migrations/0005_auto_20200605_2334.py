# Generated by Django 2.1.5 on 2020-06-05 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200605_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer_order',
            name='gbpToMntDailyRate',
            field=models.CharField(default='1', max_length=64),
        ),
    ]
