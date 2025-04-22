from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'نام کاربری قبلاً استفاده شده است')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'ثبت‌نام با موفقیت انجام شد')
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # بعداً می‌تونیم آدرس دقیق‌تری براش بذاریم
        else:
            messages.error(request, 'اطلاعات وارد شده نادرست است')
            return redirect('login')

    return render(request, 'login.html')

# صفحه کیف پول
def wallet_view(request):
    return HttpResponse("This is the wallet page")

# شارژ کردن کیف پول
def recharge_wallet(request):
    return HttpResponse("This is the recharge wallet page")

# لیست محصولات
def product_list(request):
    return HttpResponse("This is the product list page")

# داشبورد فروشنده
def seller_dashboard(request):
    return HttpResponse("This is the seller dashboard page")

# افزودن محصول
def add_product(request):
    return HttpResponse("This is the add product page")
