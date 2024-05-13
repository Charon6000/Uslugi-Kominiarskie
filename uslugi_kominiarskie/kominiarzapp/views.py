from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Kominiarz, Zamowienie
from .forms import Zamawianie, DodawanieKominiarza

def Main(request):
    return render(request, "kominiarzapp/main.html")

class Kominiarze(ListView):
    model = Kominiarz

    def get_queryset(self, *args, **kwargs):
        qs = super(Kominiarze, self).get_queryset(*args, **kwargs)
        return qs
    
class Zamowienia(ListView):
    model = Zamowienie

    def get_queryset(self, *args, **kwargs):
        qs = super(Zamowienia, self).get_queryset(*args, **kwargs)
        return qs

def ZamawianieForm(request):
    if request.method == 'POST':
        form = Zamawianie(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Main") 
    else:
        form = Zamawianie()
    context = {
        'form': form
    }
    return render(request, "kominiarzapp/zamawianie.html", context)

def KominiarzForm(request):
    if request.method == 'POST':
        form = DodawanieKominiarza(request.POST)
        if form.is_valid():
            form.save()
        return redirect("Main") 
    else:
        form = DodawanieKominiarza()
    context = {
        'form': form
    }
    return render(request, "kominiarzapp/kominiarz.html", context)
