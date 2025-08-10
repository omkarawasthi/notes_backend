from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('user_email', 'user_name', 'is_staff', 'is_active', 'created_on')
    list_filter = ('is_staff', 'is_active', 'created_on')
    
    fieldsets = (
        (None, {'fields': ('user_email', 'password')}),
        ('Personal info', {'fields': ('user_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_on')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_email', 'user_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('user_email', 'user_name')
    ordering = ('user_email',)

admin.site.register(User, CustomUserAdmin)
