from django.contrib import admin

from .models import SwitchVendor, SwitchModel, UserPlace, User


@admin.register(SwitchVendor)
class SwitchVendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(SwitchModel)
class SwitchModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'switch_vendor', 'user_place', 'ports']
    search_fields = ['title']
    list_filter = ['switch_vendor__title']


@admin.register(UserPlace)
class UserPlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'street', 'ip', 'mac', 'active']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'flat', 'installation_place']
