from django.db import models

class Contract(models.Model):
    nr_crt = models.IntegerField()
    data_contract = models.CharField(max_length=250)
    denumire_societate = models.CharField(max_length=250)
    adresa = models.CharField(max_length=250)
    cui = models.CharField(max_length=10)
    nr_rc = models.CharField(max_length=30)
    administrator = models.CharField(max_length=50)
    salarizare = models.CharField(max_length=250)
    nr_sal = models.IntegerField()
    stare_contract = models.CharField(max_length=250)
    type = models.IntegerField()
    numar_contract = models.IntegerField()

class Event(models.Model):
    date_event = models.DateField()
    id_angajat = models.IntegerField()
    html = models.TextField()

class EvidentaSalariati(models.Model):
    id_firm = models.IntegerField()
    data_save = models.DateField()
    nr_salariati = models.IntegerField()

class Message(models.Model):
    id_angajat = models.IntegerField()
    mesaj = models.CharField(max_length=500)
    date = models.DateField()
    seen = models.IntegerField()

class PdfContent(models.Model):
    pdf_id = models.IntegerField()
    pdf_content = models.CharField(max_length=10000)
    pdf_section = models.IntegerField()

class Report(models.Model):
    data_report = models.DateField()
    firm = models.CharField(max_length=250)
    angajat_id = models.IntegerField()
    html = models.CharField(max_length=20000)
    nr_t_ore = models.CharField(max_length=250)
    acte_p = models.CharField(max_length=250)
    alte_act = models.CharField(max_length=250)
    type = models.IntegerField()

class Salarizare(models.Model):
    id_firm = models.IntegerField()
    conventii = models.CharField(max_length=250)
    conventii_medicale = models.CharField(max_length=250)
    dosar_somaj = models.CharField(max_length=250)
    conventii_noi = models.CharField(max_length=250)
    alte_dosare = models.CharField(max_length=250)

class SituatieLunara(models.Model):
    id_angajat = models.IntegerField()
    id_firm = models.CharField(max_length=250)
    json = models.TextField()
    stare = models.IntegerField()
    data_trimitere = models.DateField()

class User(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    type = models.IntegerField()
    acces = models.IntegerField(null=True)
    acces_lunar = models.IntegerField()