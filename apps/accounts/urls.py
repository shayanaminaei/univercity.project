from django.urls import path
from . import views
from django.urls import include
urlpatterns = [
   path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
