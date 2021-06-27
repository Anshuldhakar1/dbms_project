from django.contrib import admin

from .models import User, Listing, Category, Bid, Order, Comment, Watchlist

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','contact_no')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','user','Title','Category','Active')

class CateAdmin(admin.ModelAdmin):
    list_display = ('id','category')

class BidAdmin(admin.ModelAdmin):
    list_display = ('id','listing','bidder','bid')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','By','action')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','listing','commentor','comment')
    
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id','user')

admin.site.register(User,UserAdmin)
admin.site.register(Listing,ListingAdmin)
admin.site.register(Category,CateAdmin)
admin.site.register(Bid,BidAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Watchlist,WatchlistAdmin)