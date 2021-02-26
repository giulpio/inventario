# Generated by Django 3.1.2 on 2020-10-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cod', models.CharField(max_length=100, verbose_name='Numero Articolo')),
                ('classe', models.CharField(max_length=100)),
                ('mod_stoccaggio', models.TextField()),
                ('tds', models.FileField(blank=True, null=True, upload_to='tds/')),
                ('sds', models.FileField(blank=True, null=True, upload_to='sds/')),
                ('note_zdhc', models.TextField(blank=True)),
                ('certificazioni', models.TextField(blank=True)),
                ('conf_zdhc', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]