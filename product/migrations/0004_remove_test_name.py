# Generated by Django 3.1.2 on 2020-12-20 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201123_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='name',
        ),
    ]
