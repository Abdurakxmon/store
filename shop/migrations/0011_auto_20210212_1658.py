# Generated by Django 3.1.5 on 2021-02-12 11:58

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_cart_cartproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.post'),
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(default=datetime.datetime(2021, 2, 12, 11, 58, 36, 626899, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
