# Generated by Django 3.2.9 on 2022-02-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20220203_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodations',
            name='occupancy',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
