# Generated by Django 4.2.1 on 2023-05-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0012_alter_filter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('20000 to 30000', '20000 to 30000'), ('5000 to 10000', '5000 to 10000'), ('10000 to 15000', '10000 to 15000'), ('100 to 5000', '100 to 5000'), ('15000 to 20000', '15000 to 20000')], max_length=60),
        ),
    ]
