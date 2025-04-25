from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserRegistrationForm, UserLoginForm, WalletTopUpForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Wallet, UserProfile


# Create your views here.
def home(request):
    return HttpResponse("dorood, accounts app work well :) ")

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "ثبت‌نام شما با موفقیت انجام شد!")
            return redirect('login')  # بعد از ثبت‌نام، به صفحه ورود هدایت می‌شود
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ثبت‌نام با موفقیت انجام شد")
            return redirect('login')  # به صفحه ورود بعد از ثبت‌نام هدایت می‌کنیم
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# ورود
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "ورود شما با موفقیت انجام شد!")
                return redirect('home')  # بعد از ورود، به صفحه اصلی هدایت می‌شود
            else:
                messages.error(request, "ایمیل یا رمز عبور نادرست است.")
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def wallet_topup(request):
    if request.method == 'POST':
        form = WalletTopUpForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            wallet = Wallet.objects.get(user=request.user)
            wallet.balance += amount
            wallet.save()
            return redirect('profile')  # بعد از شارژ کیف پول کاربر به صفحه پروفایل هدایت می‌شود
    else:
        form = WalletTopUpForm()
    
    return render(request, 'accounts/wallet_topup.html', {'form': form})

def wallet_topup_view(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        form = WalletTopUpForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            if amount is not None:
                profile.wallet += amount
                profile.save()
                return redirect('home')  # یا هر آدرس دلخواه
            else:
                form.add_error('amount', 'مقدار شارژ نمی‌تواند خالی باشد.')
    else:
        form = WalletTopUpForm()

    return render(request, 'wallet_topup.html', {'form': form})

def profile_view(request):
    wallet, created = Wallet.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'wallet': wallet
    })
    
def logout_view(request):
    logout(request)
    return redirect('home')  # یا صفحه‌ی دلخواه شما بعد از خروج

def home_view(request):
    # اینجا می‌تونید لیستی از صفحات خودتون رو داشته باشید
    pages = [
        {"name": "پروفایل", "url": "profile"},
        {"name": "شارژ کیف پول", "url": "wallet_topup"},
        {"name": "صفحه اصلی", "url": "home"},
        {"name": "خروج", "url": "logout"},
    ]
    return render(request, 'home.html', {'pages': pages})