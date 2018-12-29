from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.account.models import User, UserProfile



@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    readonly_fields = ["username", "last_login", "date_joined", "password"]

class Profile(admin.ModelAdmin):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
