# Generated by Django 3.1.7 on 2021-02-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='message',
            field=models.TextField(blank=True, verbose_name='Additional_message'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tm_id',
            field=models.CharField(blank=True, max_length=50, verbose_name='tm_id'),
        ),
    ]
