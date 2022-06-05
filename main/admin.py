from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from . models import Account, Orders

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Данные аккаунта'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInline, )

# Register your models here.

admin.site.unregister(User)

admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Orders)

# Register your models here.
