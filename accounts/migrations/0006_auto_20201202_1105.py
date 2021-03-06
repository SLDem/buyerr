# Generated by Django 3.1.3 on 2020-12-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201202_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Delivery Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Phone'),
        ),
    ]
