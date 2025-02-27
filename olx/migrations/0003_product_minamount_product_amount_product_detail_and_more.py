# Generated by Django 5.0.6 on 2024-07-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Minamount',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
