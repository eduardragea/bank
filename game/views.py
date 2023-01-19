from django.shortcuts import render, redirect
from .models import BankModel, User
from .forms import SignUpForm, LogInForm, NewBankForm
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
            club = BankModel.objects.create(name=name, fullName=fullName, owner=user)
            return redirect('dashboard')
    else:
        form = NewBankForm()
    return render(request, 'new_bank.html', {'form': form})

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
