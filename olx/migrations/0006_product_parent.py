# Generated by Django 5.0.6 on 2024-07-07 16:45

import django.db.models.deletion
import mptt.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0005_color_size_rename_minamount_product_minamount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='olx.product'),
        ),
    ]
