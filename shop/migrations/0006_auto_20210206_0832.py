# Generated by Django 3.1.5 on 2021-02-06 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210205_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hot',
            field=models.BooleanField(default=False, verbose_name='Hot'),
        ),
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=True, verbose_name='Yangi'),
        ),
        migrations.AddField(
            model_name='product',
            name='special',
            field=models.BooleanField(default=False, verbose_name='Maxsus taklif'),
        ),
    ]
