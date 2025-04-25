from django.contrib import admin
from django.urls import path, include
from apps.accounts import views 
# include برای اضافه کردن مسیرهای اپلیکیشن‌ها

urlpatterns = [
    path('admin/', admin.site.urls),  # مسیر پیش‌فرض برای پنل مدیریت جنگو
    path('accounts/', include('accounts.urls')),  # شامل کردن مسیرهای login و register از accounts
    # مسیرهای دیگر مربوط به وب‌سایت
    path('wallet/', views.wallet_view, name='wallet_view'),
    path('recharge/', views.recharge_wallet, name='recharge_wallet'),
    path('products/', views.product_list, name='product_list'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('seller/add-product/', views.add_product, name='add_product'),
]
