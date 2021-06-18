from django.contrib import admin

from .models import User, Listing, Category

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','user','Title','Category','Active')

class CateAdmin(admin.ModelAdmin):
    list_display = ('id','category')

admin.site.register(User,UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Category,CateAdmin)