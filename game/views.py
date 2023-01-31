from django.shortcuts import render, redirect
from .models import BankModel, User, YearModel
from .forms import SignUpForm, LogInForm, NewBankForm, NewYearForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden
from .helpers import login_prohibited
import datetime

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    banks = BankModel.objects.all()
    user = request.user
    bank = None
    for b in banks:
        if b.owner == user:
            bank = b
            break
    return render(request, 'dashboard.html', {'banks': banks, 'current_user': user, 'bank': bank})

@login_required
def new_bank(request):
    user = request.user
    if request.method == 'POST':
        form = NewBankForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            fullName = form.cleaned_data.get('fullName')
            club = BankModel.objects.create(name=name, fullName=fullName, owner=user,b75=90.0, b76=0.0, b77=0.0, b78=10.0, b111=0.2, c89=10.0, c85=0.0, c84=90.0, b108=0.0, year=0)
            return redirect('dashboard')
    else:
        form = NewBankForm()
    return render(request, 'new_bank.html', {'form': form})

@login_required
def new_year(request):
    user = request.user
    bank = BankModel.objects.get(owner=user)
    # if request.method == 'POST':
        # form = NewYearForm(request.POST)
        # if form.is_valid():
        #     b5 = form.cleaned_data.get('b5')
        #     club = BankModel.objects.create(b5=b5, owner=user)
        #     return redirect('dashboard')
    # if 'd4' in request.POST:
    #     d5 = request.POST['d4']
    # else:
    #     d5 = False
    d75 = request.POST.get('d75')
    d76 = request.POST.get('d76')
    d77 = request.POST.get('d77')
    d78 = request.POST.get('d78')
    d111 = request.POST.get('d111')
    e89 = request.POST.get('e89')
    e84 = request.POST.get('E84')
    e85 = request.POST.get('E85')
    d108 = request.POST.get('D108')
    newYear = bank.year+1
    year = YearModel.objects.create(d75=d75, d76=d76, d77=d77, d78=d78, d111=d111, e89=e89, e85=e85, e84=e84, d108=d108, year=newYear,bank=bank)
    BankModel.objects.filter(owner=user).update(b75=d75, b76=d76, b77=d77, b78=d78, b111=d111, c89=e89, c85=e85, c84=e84, b108=d108, year=newYear)
    # return redirect('dashboard')
    # else:
    #     form = NewYearForm()
    # return render(request, 'new_bank.html', {'form': form})
    return redirect('dashboard')

def log_out(request):
    logout(request)
    return redirect('home')

@login_prohibited
def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        next = request.POST.get('next') or ''
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                redirect_url = next or 'dashboard'
                return redirect(redirect_url)
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    else:
        next = request.GET.get('next') or ''
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form, 'next': next})

@login_prohibited
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('log_in')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})
