# Generated by Django 4.0.6 on 2022-07-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prdlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_name', models.CharField(max_length=30)),
                ('prd_cat', models.CharField(max_length=100)),
                ('prd_subcat', models.CharField(max_length=100)),
                ('prd_des', models.CharField(max_length=200)),
                ('prd_date', models.DateField()),
                ('prd_img', models.ImageField(upload_to='shop/images')),
                ('prd_cost', models.IntegerField()),
            ],
        ),
    ]
