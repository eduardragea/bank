from django.shortcuts import render, redirect
from .models import BankModel
from .forms import NewBankForm

def home(request):
    banks = BankModel.objects.all()
    return render(request, 'dashboard.html', {'banks': banks})

def new_bank(request):
    if request.method == 'POST':
        form = NewBankForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            fullName = form.cleaned_data.get('fullName')
            club = BankModel.objects.create(name=name, fullName=fullName)
            return redirect('home')
    else:
        form = NewBankForm()
    return render(request, 'new_bank.html', {'form': form})
