from django.contrib import admin
from account.models import Account



class AccountAdmin(admin.ModelAdmin):

    list_display=('first_name','last_name','email','username',)


admin.site.register(Account,AccountAdmin)
# Register your models here.
