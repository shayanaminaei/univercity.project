from django.contrib import admin
from .models import CustomUser

# Register CustomUser in admin panel
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'username']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)
