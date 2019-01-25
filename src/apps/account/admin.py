from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.account.models import User, City, RequestDayOff
from apps.account.forms import UserAdminForm
from django import forms
from apps import model_choices as mch


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    pass

@admin.register(RequestDayOff)
class RequestDayOffAdmin(admin.ModelAdmin):
    list_filter = ('status', 'type')
    readonly_fields = ('user', 'type')
    # TODO add form
    # TODO subtract dayoffs or vacations on Form Approve

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(self, request)
        if obj is not None:
            # if request.user.is_hr:  # check if request user in group
            # if obj.status != mch.STATUS_PENDING and not request.user.is_superuser:  # allow superuser to change status field
            if obj.status != mch.STATUS_PENDING:
                readonly_fields += ('status', )
                # readonly_fields = readonly_fields + ('status', )
        return readonly_fields


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    readonly_fields = []
    list_display = ['id', 'username', 'email', 'age']
    list_filter = ['date_joined', 'last_login', 'age']
    list_per_page = 10
    search_fields = ['email', 'first_name', 'phone']
    # form = UserAdminForm

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['username', 'last_login', 'date_joined', 'password']
        return []

    def get_form(self, request, obj=None, **kwargs):
        if obj is None: #add user form
            return UserAdminForm
        else:#for existing users
            return super().get_form(request, obj, **kwargs)

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            return not obj.is_superuser
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.exclude(is_superuser=True)
        return qs






