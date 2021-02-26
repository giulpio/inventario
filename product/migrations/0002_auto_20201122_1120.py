# Generated by Django 3.1.2 on 2020-11-22 11:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fasi_produzione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Hazard_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Manifacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pictogram_dpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='static/pittogrammi/')),
            ],
        ),
        migrations.CreateModel(
            name='Pictogram_h',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='static/pittogrammi/')),
            ],
        ),
        migrations.CreateModel(
            name='Precautionary_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='note_zdhc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sds',
            field=models.FileField(blank=True, null=True, upload_to='static/sds/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tds',
            field=models.FileField(blank=True, null=True, upload_to='static/tds/'),
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
                ('t_date', models.DateField(default=datetime.date.today)),
                ('descr', models.TextField()),
                ('ap_apeo', models.BooleanField()),
                ('clorobenzeni_clorutolenti', models.BooleanField()),
                ('clorofenoli', models.BooleanField()),
                ('ammine_aromatiche', models.BooleanField()),
                ('coloranti_dispersi', models.BooleanField()),
                ('coloranti_cancerogeni', models.BooleanField()),
                ('navy_blue', models.BooleanField()),
                ('ritardanti_fiamma', models.BooleanField()),
                ('glicoli', models.BooleanField()),
                ('solventi', models.BooleanField()),
                ('organostannici', models.BooleanField()),
                ('idricarburi_policiclici_aromatici', models.BooleanField()),
                ('voc', models.BooleanField()),
                ('ftalati', models.BooleanField()),
                ('pfc', models.BooleanField()),
                ('metalli_pesanti', models.BooleanField()),
                ('rapporto', models.FileField(blank=True, null=True, upload_to='rapporti/')),
                ('scadenza_rapporto', models.DateField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Concentrazioni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('concentrazione', models.FloatField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sostanze', to='product.product')),
            ],
            options={
                'db_table': 'sostanza',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='fasi_produzione',
            field=models.ManyToManyField(blank=True, to='product.Fasi_produzione'),
        ),
        migrations.AddField(
            model_name='product',
            name='fornitore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.seller', to_field='name'),
        ),
        migrations.AddField(
            model_name='product',
            name='frasi_h',
            field=models.ManyToManyField(blank=True, related_name='prodotti', to='product.Hazard_Statement'),
        ),
        migrations.AddField(
            model_name='product',
            name='frasi_p',
            field=models.ManyToManyField(blank=True, related_name='prodotti', to='product.Precautionary_Statement'),
        ),
        migrations.AddField(
            model_name='product',
            name='pittogrammi_dpi',
            field=models.ManyToManyField(blank=True, to='product.Pictogram_dpi'),
        ),
        migrations.AddField(
            model_name='product',
            name='pittogrammi_hazard',
            field=models.ManyToManyField(blank=True, to='product.Pictogram_h'),
        ),
        migrations.AddField(
            model_name='product',
            name='produttore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.manifacturer', to_field='name'),
        ),
    ]
