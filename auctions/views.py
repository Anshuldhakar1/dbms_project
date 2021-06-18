from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Order

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
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")