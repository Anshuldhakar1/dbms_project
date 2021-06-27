from django.contrib import admin

from .models import User, Listing, Category, Bid, Order, Comment, Watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Watchlist)

# class ListingAdmin(admin.ModelAdmin):
#     model = Listing
#     list_display = ['user','Title','Category','Description','Image','Bid','Active','Time'] 
#     list_editable = ['user','Title','Category','Description','Image','Bid','Active','Time'] 
#     # list_editable = ['quantity', 'description', 'tax_rate', ] 