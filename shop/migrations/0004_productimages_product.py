# Generated by Django 3.1.5 on 2021-02-05 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
