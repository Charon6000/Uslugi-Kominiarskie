from django.db import models

# Create your models here.
class Zamowienie(models.Model):
    kominiarz = models.ForeignKey('Kominiarz', on_delete=models.SET_NULL, null=True)
    miasto = models.CharField(max_length=20)
    ulica = models.CharField(max_length=20)
    numerdomu = models.IntegerField()
    numermieszkania = models.IntegerField()
    dzien = models.DateField()

    def __str__(self):
        return str(self.id)

class Kominiarz(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    wiek = models.IntegerField()
    opis = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
