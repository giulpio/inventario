# Generated by Django 3.1.2 on 2021-02-23 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20210207_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='conf_zdhc',
        ),
    ]
