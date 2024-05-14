from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def Rejestracja(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("Main")
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/Rejestracja.html', context)

@csrf_protect
def Logowanie(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("Main")
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/Logowanie.html', context)

@csrf_protect
def Wylogowywanie(request):
    if request.method == 'POST':
        logout(request)
        return redirect("Main")