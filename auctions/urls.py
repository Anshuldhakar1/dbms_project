from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    # path("createListing", views.create_listing, name="create_listing"),
    # path("listings/<str:list_Title>", views.view_listing, name="listing"),
    # path("listings/<str:list_Title>/edit", views.edit_listing, name="edit_list"),
    # path("listings/<str:list_Title>/update", views.list_update, name="update"),
    # path("listings/<str:list_Title>/comment", views.comment, name="comment"),
    # path("categories", views.categories, name="categories"),
    # path("categories/<str:category>", views.get_category, name="get_category"),
    # path("<str:username>", views.user_view, name="user"),
    # path("<str:username>/watchlist", views.watchlist, name="watchlist")
]
