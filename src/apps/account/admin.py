from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.account.models import User, City
from django import forms


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    pass

# @admin.register(Contact_us)
# class Contactus.Admin(admin.ModelAdmin):
#
#     pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    readonly_fields = ["username", "last_login", "date_joined", "password"]


    list_display = ['id', 'username', 'email', 'age']
    list_filter = ['date_joined', 'last_login', 'age']
    search_fields = ['email', 'first_name', 'phone']

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            return not obj.is_superuser
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.exclude(is_superuser=True)
        return qs






