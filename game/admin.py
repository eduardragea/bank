"""Configuration of admin interface for clubs."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import BankModel, User, YearModel


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model to allow email for username"""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('id', 'email', 'first_name', 'last_name',)
    search_fields = ('id', 'email', 'first_name', 'last_name')
    ordering = ('id',)

@admin.register(BankModel)
class BankModelAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for ClubModel."""

    list_display = [
        'id', 'name', 'owner', 'b75','b76','b77','b78','b111','c84','c85','c89', 'b108', 'year'
    ]

@admin.register(YearModel)
class YearModelAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for ClubModel."""

    list_display = [
        'd75','d76','d77','d78','d111','e84','e85','e89', 'd108', 'year', 'bank'
    ]
