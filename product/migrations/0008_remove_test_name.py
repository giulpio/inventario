# Generated by Django 3.1.2 on 2020-12-20 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20201220_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='name',
        ),
    ]
