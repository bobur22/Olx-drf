# Generated by Django 5.1.2 on 2024-11-06 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0007_alter_product_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(choices=[('remote', 1), ('office', 2)], default='office', max_length=20)),
                ('posted_on', models.DateField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
