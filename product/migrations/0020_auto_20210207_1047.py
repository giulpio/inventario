# Generated by Django 3.1.2 on 2021-02-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_product_sds_rev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stato_arte',
            field=models.CharField(choices=[('ON', 'Attivo'), ('PROVA', 'Prova'), ('OFF', 'Fuori uso')], default='PROVA', max_length=10),
        ),
    ]
