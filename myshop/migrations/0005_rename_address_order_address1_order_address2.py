# Generated by Django 4.0.6 on 2022-08-04 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(default='', max_length=200),
        ),
    ]
