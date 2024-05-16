from django import forms
from django.core.exceptions import ValidationError
from .models import Zamowienie, Kominiarz

class Zamawianie(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        numerdomu = cleaned_data.get('numerdomu')
        numermieszkania = cleaned_data.get('numermieszkania')
        
        if not isinstance(numerdomu, int) or not isinstance(numermieszkania, int):
            raise ValidationError("Numer domu i mieszkania musi być liczbą.")
        
        return cleaned_data

    class Meta:
        model = Zamowienie
        fields = ['kominiarz', 'miasto', 'ulica', 'numerdomu', 'numermieszkania', 'dzien']
        widgets = {
        'dzien': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Wybierz date', 'type':'date'}),
    }

class DodawanieKominiarza(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        wiek = cleaned_data.get('wiek')
        
        if not isinstance(wiek, int):
            raise ValidationError("Wiek musi być liczbą.")
        
        return cleaned_data

    class Meta:
        model = Kominiarz
        fields = ['imie', 'nazwisko', 'wiek', 'opis', 'zdj']
