# Generated by Django 3.1.2 on 2021-01-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20210106_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sds_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]