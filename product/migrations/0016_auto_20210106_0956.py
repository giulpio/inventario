# Generated by Django 3.1.2 on 2021-01-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20210106_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificazioni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gateway_zdhc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='certificazioni',
        ),
    ]