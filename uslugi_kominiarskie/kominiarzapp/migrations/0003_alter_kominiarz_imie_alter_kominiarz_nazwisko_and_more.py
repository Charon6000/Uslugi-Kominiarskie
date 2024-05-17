# Generated by Django 5.0.4 on 2024-05-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kominiarzapp', '0002_kominiarz_zdj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kominiarz',
            name='imie',
            field=models.CharField(max_length=20, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='kominiarz',
            name='nazwisko',
            field=models.CharField(max_length=20, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='kominiarz',
            name='opis',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='kominiarz',
            name='wiek',
            field=models.IntegerField(verbose_name='Wiek'),
        ),
        migrations.AlterField(
            model_name='kominiarz',
            name='zdj',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='Zdjęcie'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='dzien',
            field=models.DateField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='miasto',
            field=models.CharField(max_length=20, verbose_name='Miasto'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='numerdomu',
            field=models.IntegerField(verbose_name='Numer Domu'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='numermieszkania',
            field=models.IntegerField(blank=True, default='', null=True, verbose_name='Numer Mieszkania'),
        ),
        migrations.AlterField(
            model_name='zamowienie',
            name='ulica',
            field=models.CharField(max_length=20, verbose_name='Ulica'),
        ),
    ]
