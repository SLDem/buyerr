# Generated by Django 3.1.4 on 2020-12-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
