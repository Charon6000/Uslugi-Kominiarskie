from django.db import models

# Create your models here.
class Zamowienie(models.Model):
    kominiarz = models.ForeignKey('Kominiarz', on_delete=models.SET_NULL, null=True)
    miasto = models.CharField("Miasto", max_length=20)
    ulica = models.CharField("Ulica", max_length=20)
    numerdomu = models.IntegerField("Numer Domu")
    numermieszkania = models.IntegerField("Numer Mieszkania",null=True, default="", blank=True)
    dzien = models.DateField("Data")

    def __str__(self):
        return str(self.id)

class Kominiarz(models.Model):
    imie = models.CharField("Imię", max_length=20)
    nazwisko = models.CharField("Nazwisko",max_length=20)
    wiek = models.IntegerField("Wiek")
    opis = models.CharField("Opis",max_length=1000,null=True, default="", blank=True)
    zdj = models.CharField("Zdjęcie",max_length=1000,null=True, default="", blank=True)

    def __str__(self):
        return str(self.imie) + " " +str(self.nazwisko)
