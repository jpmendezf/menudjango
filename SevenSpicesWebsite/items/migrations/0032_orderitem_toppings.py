# Generated by Django 2.1.2 on 2018-12-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0031_auto_20181209_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='items.Topping'),
        ),
    ]
