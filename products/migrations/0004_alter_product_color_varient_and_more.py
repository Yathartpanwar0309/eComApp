# Generated by Django 4.2.7 on 2023-11-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_colorvarient_price_sizevarient_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color_varient',
            field=models.ManyToManyField(blank=True, to='products.colorvarient'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_varient',
            field=models.ManyToManyField(blank=True, to='products.sizevarient'),
        ),
    ]
