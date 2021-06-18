from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from datetime import date
import time 

from .models import User, Listing, Category, Bid, Order, Comment, Watchlist

def index(request):
    listings = Listing.objects.all()
    sort_by = "Default"

    if request.method == "POST":
        sort_by = request.POST["order"]

    order = Order.objects.get(By=sort_by).action

    if sort_by == "Default":
        listings = Listing.objects.all()
    elif order == "special1":
        listings = Listing.objects.order_by('Date', 'Time')
    elif order == "special2":
        listings = Listing.objects.order_by('-Date', '-Time')
    else:
        listings = Listing.objects.order_by(order)

    try:
        watchlist_listings = User.objects.get(username=request.user.username).watchlist.listings.all()
        return render(request, "auctions/index.html", {
            "listings": listings,
            "sel_order": sort_by,
            "orders": Order.objects.all(),
            "check_watchlist": True,
            "watchlist_listings": watchlist_listings
        })
    except:
        return render(request, "auctions/index.html", {
            "listings": listings,
            "sel_order": sort_by,
            "orders": Order.objects.all(),
            "check_watchlist": False
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match"
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            watch_list = Watchlist(user=user)
            watch_list.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

# @login_required(login_url="login")
# def view_listing(request, list_Title):
#     try:
#         List = Listing.objects.get(Title=list_Title)
#     except:
#         return render(request, "auctions/error.html", {
#             "code": 404,
#             "message": "The page you requested does not exist."
#         })

#     in_watchlist = False
#     user = request.user
#     watchlist_listings = user.watchlist.listings.all()
#     if List in watchlist_listings:
#         in_watchlist = True

#     if request.method == "POST":

#         if  not float(request.POST["list_bid"]) > List.Bid.bid:
#             print(List.Bid.bidder)
#             return render(request, "auctions/listing.html", {
#                 "listing": List,
#                 "message": "The Bid MUST be greater than the previous",
#                 "comments": Comment.objects.filter(listing__Title=list_Title),
#                 "in_watchlist": in_watchlist
#             })

#         bid = Bid.objects.get(listing=List)
#         bid.bid = float(request.POST["list_bid"])
#         bid.bidder = request.user
#         bid.save()

#         return HttpResponseRedirect(reverse("listing", args=(List.Title,)))

#     return render(request, "auctions/listing.html", {
#         "listing": List,
#         "comments": Comment.objects.filter(listing__Title=list_Title),
#         "in_watchlist": in_watchlist
#     })

# @login_required(login_url="login")
# def create_listing(request):
#     if request.method == "GET":
#         return render(request, "auctions/create_listing.html", {
#             "categories": Category.objects.all()
#         })
#     listing = Listing()
#     new_list = request.POST
#     listing.Title = new_list["list_title"]

#     # Checking title

#     for list_obj in Listing.objects.all():
#         if list_obj.Title == listing.Title:
#             return render(request, "auctions/create_listing.html", {
#                 "message": "This title exists please use another"
#             })  
 
#     listing.Description = new_list["list_desc"]

#     bid = Bid(bid = float(new_list["list_bid"]))
#     bid.save()
#     listing.Bid = bid

#     listing.Image = new_list["list_img"]
#     listing.Category = Category.objects.get(category=new_list["list_category"])
#     listing.Date = date.today()
#     listing.Time = time.strftime("%H:%M:%S", time.localtime())
#     listing.user = User.objects.get(username=request.user.username)
#     listing.save()
#     return HttpResponseRedirect(reverse("listing", args=(listing.Title,)))

# @login_required(login_url="login")
# def edit_listing(request, list_Title):
#     List = Listing.objects.get(Title=list_Title)
#     if not List.user.username == request.user.username:
#         return render(request, "auctions/error.html", {
#             "code": 403,
#             "message": "You are not authorised to access this page"
#         })
#     if request.method == "POST":
#         List.Title = request.POST["list_title"]
#         List.Description = request.POST["list_desc"]

#         bid = Bid.objects.get(listing=List)
#         bid.bid = float(request.POST["list_bid"])
#         bid.bidder = None
#         bid.save()

#         List.Image = request.POST["list_img"]
#         List.Category = Category.objects.get(category=request.POST["list_category"])
#         List.save()
#         return HttpResponseRedirect(reverse("listing", args=(List.Title,)))
    
#     return render(request, "auctions/edit_listing.html", {
#         "listing": List,
#         "categories": Category.objects.all()
#     })

# @login_required(login_url="login")
# def list_update(request, list_Title):
#     if request.method == "GET":
#         return render(request, "auctions/error.html", {
#             "code": 403,
#             "message": "Forbidden. No one can access this page"
#         })
#     listing = Listing.objects.get(Title=list_Title)
#     if not listing.user.username == request.user.username:
#         return render(request, "auctions/error.html", {
#             "code": 403,
#             "message": "You are not authorised to access this page"
#         })
        
#     if "is_active" in request.POST:
#         listing.Active = True
#     else:
#         listing.Active = False
#     listing.save()
#     return redirect(request.POST["prev_page"])

# @login_required(login_url="login")
# def comment(request, list_Title):
#     listing = Listing.objects.get(Title=list_Title)
#     print(request.POST)
#     new_comment = Comment()
#     new_comment.listing = Listing.objects.get(Title=list_Title)
#     new_comment.commentor = User.objects.get(username=request.POST["user"])
#     new_comment.comment = request.POST["new_comment"]
#     new_comment.save()
#     return HttpResponseRedirect(reverse("listing", args=(listing.Title,)))

# @login_required(login_url="login")
# def categories(request):
#     if request.method == "POST":
#         try:
#             request.POST["add_category"]
#             cat = Category()
#             cat.category = request.POST["category"]
#             cat.save()
#             return HttpResponseRedirect(reverse("categories"))
#         except:
#             return render(request, "auctions/categories.html", {
#                 "categories": Category.objects.all(),
#                 "add_category": True
#             })
#     return render(request, "auctions/categories.html", {
#         "categories": Category.objects.all()
#     })

# @login_required(login_url="login")
# def get_category(request, category):
#     watchlist_listings = User.objects.get(username=request.user.username).watchlist.listings.all()
#     print(watchlist_listings)
#     return render(request, "auctions/category.html", {
#         "category": category,
#         "listings": Category.objects.get(category=category).listings.all(),
#         "check_watchlist": True,
#         "watchlist_listings": watchlist_listings
#     })

# @login_required(login_url="login")
# def user_view(request, username):
#     if not request.user.username == username:
#         return render(request, "auctions/error.html", {
#             "code": 403,
#             "message": "You are not authorised to access this page"
#         })
#     if request.method == "POST":
#         print(Comment.objects.filter(commentor__username=username))
#         return render(request, "auctions/user.html", {
#             "user": User.objects.get(username=username),
#             "listings": User.objects.get(username=username).listings.all(),
#             "show_comments": True,
#             "comments": Comment.objects.filter(commentor__username=username)
#         })
#     return render(request, "auctions/user.html", {
#         "user": User.objects.get(username=username),
#         "listings": User.objects.get(username=username).listings.all()
#     })

# @login_required(login_url="login")
# def watchlist(request, username):
#     if not request.user.username == username:
#         return render(request, "auctions/error.html", {
#             "code": 403,
#             "message": "You are not authorised to access this page"
#         })
#     user = User.objects.get(username=username)
#     if request.method == "GET":
#         return render(request, "auctions/watchlist.html", {
#             "listings": user.watchlist.listings.all()
#         })
#     else:
#         if "Add_watchlist" in request.POST:
#             listing = Listing.objects.get(Title=request.POST["list_title"])
#             user.watchlist.listings.add(listing)
#             return HttpResponseRedirect(reverse("watchlist", args=(username,)))
#         else:
#             listing = Listing.objects.get(Title=request.POST["list_title"])
#             user.watchlist.listings.remove(listing)
#             return HttpResponseRedirect(reverse("watchlist", args=(username,)))