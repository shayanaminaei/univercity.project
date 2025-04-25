from django.urls import path
from . import views
from .views import register_view, wallet_topup_view, profile_view, user_logout, home_view


urlpatterns = [
    #path('', views.home, name='home'),
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('wallet/topup/', wallet_topup_view, name='wallet_topup'),
    path('profile/', profile_view, name='profile'),
]

