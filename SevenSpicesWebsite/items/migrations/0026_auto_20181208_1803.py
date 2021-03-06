# Generated by Django 2.1.2 on 2018-12-08 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0025_auto_20181208_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='delivered_to_address',
        ),
        migrations.AddField(
            model_name='address',
            name='orders',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='items.Order'),
        ),
    ]
