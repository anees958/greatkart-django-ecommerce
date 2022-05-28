from django.contrib import admin
from account.models import Account,UserProfile
from django.utils.html import format_html



class AccountAdmin(admin.ModelAdmin):

    list_display=('first_name','last_name','email','username',)

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
# Register your models here.
