from django.db import models
from PIL import Image
from django.urls import reverse

# Create your models here.
import datetime

# frasi P


class Precautionary_Statement(models.Model):
    code = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('frasi_h_p-list')


# frasi H
class Hazard_Statement(models.Model):
    code = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('frasi_h_p-list')


class Manifacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('MS-list')


class Seller(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('MS-list')


class Pictogram_h(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='pittogrammi/')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('pittogrammi-list')


class Pictogram_dpi(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='pittogrammi/')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('pittogrammi-list')


class Fasi_produzione(models.Model):
    name = models.CharField(max_length=25)
   # id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fasi-list')


class Gateway_zdhc(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Certificazioni(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    #active = models.BooleanField(default=True)
    stato_arte = models.CharField(
        max_length=10,
        choices=[('ON', 'Attivo'), ('PROVA', 'Prova'), ('OFF', 'Fuori uso')],
        default='PROVA',
    )
    cod = models.CharField('Numero Articolo', max_length=100)
    classe = models.CharField(max_length=100)
    fornitore = models.ForeignKey(
        Seller, on_delete=models.SET_NULL, to_field='name', null=True, blank=True)
    produttore = models.ForeignKey(
        Manifacturer, on_delete=models.SET_NULL, to_field='name', null=True)
    mod_stoccaggio = models.TextField()
    tds = models.FileField(upload_to='tds/', blank=True, null=True)
    sds = models.FileField(upload_to='sds/', blank=True, null=True)
    sds_date = models.DateField(auto_now=False, blank=True, null=True)
    sds_rev = models.CharField(
        'Revisione', max_length=50, blank=True, null=True)
    #sostanze=models.ManyToManyField(Concentrazioni, blank=True)
    # sostanze=models.TextField(blank=True)
    #concentrazione=models.FloatField(null=True, blank=True)
    #note_zdhc = models.TextField(blank=True, null=True)
    #certificazioni = models.TextField(blank=True)
    #conf_zdhc = models.CharField(max_length=100, blank=True)
    gateway = models.ManyToManyField(Gateway_zdhc, blank=True)
    certificazioni = models.ManyToManyField(Certificazioni, blank=True)
    #conf_zdhc = models.BooleanField(default=False)
    conf_zdhc = models.CharField(
        max_length=10,
        choices=[('SI', 'Conforme'), ('NO', 'Non Conforme'), ('NA', 'NA')],
        default='NA',
    )
    frasi_h = models.ManyToManyField(
        Hazard_Statement, related_name='prodotti', blank=True)
    frasi_p = models.ManyToManyField(
        Precautionary_Statement, related_name='prodotti', blank=True)
    pittogrammi_hazard = models.ManyToManyField(Pictogram_h, blank=True)
    pittogrammi_dpi = models.ManyToManyField(Pictogram_dpi, blank=True)
    fasi_produzione = models.ManyToManyField(Fasi_produzione, blank=True)
    concentrazioni = models.JSONField(default=dict)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class test(models.Model):
    #name = models.CharField(max_length=100, blank=True)
    t_date = models.DateField(default=datetime.date.today)
    descr = models.TextField()
    ap_apeo = models.BooleanField()
    clorobenzeni_clorutolenti = models.BooleanField()
    clorofenoli = models.BooleanField()
    ammine_aromatiche = models.BooleanField()
    coloranti_dispersi = models.BooleanField()
    coloranti_cancerogeni = models.BooleanField()
    navy_blue = models.BooleanField()
    ritardanti_fiamma = models.BooleanField()
    glicoli = models.BooleanField()
    solventi = models.BooleanField()
    organostannici = models.BooleanField()
    idricarburi_policiclici_aromatici = models.BooleanField()
    voc = models.BooleanField()
    ftalati = models.BooleanField()
    pfc = models.BooleanField()
    metalli_pesanti = models.BooleanField()

    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    rapporto = models.FileField(upload_to='rapporti/', blank=True, null=True)
    scadenza_rapporto = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('test-list')


class Concentrazioni(models.Model):
    name = models.CharField(max_length=100, blank=True)
    concentrazione = models.FloatField(null=True, blank=True)
    product = models.ForeignKey(
        Product, related_name='sostanze', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'sostanza'

    def __str__(self):
        return self.name
