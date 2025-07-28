from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserChangeForm, UserCreateForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('email', 'phone_number', 'full_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Main', {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'email', 'full_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('phone_number', 'full_name')
    ordering = ('full_name',)
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)