from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Kominiarz, Zamowienie
from .forms import Zamawianie

def Main(request):
    return render(request, "kominiarzapp/main.html")

class Kominiarze(ListView):
    model = Kominiarz

    def get_queryset(self, *args, **kwargs):
        qs = super(Kominiarze, self).get_queryset(*args, **kwargs)
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
