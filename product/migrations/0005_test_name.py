# Generated by Django 3.1.2 on 2020-12-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_test_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
