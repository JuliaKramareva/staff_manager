from django.contrib import admin
from apps.account.models import User



@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    readonly_fields = ["username", "last_login", "date_joined", "password"]