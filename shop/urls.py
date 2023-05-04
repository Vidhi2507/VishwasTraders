from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.index,name="shophome"),
    path('about/',views.about,name="aboutUs"),
    path('contactus/',views.contact,name="ContactUs"),
     path("products/<int:myid>", views.productView, name="ProductView"),
    path('search/',views.search,name="search"),
    path('checkout/',views.checkout,name="checkout"),
    path('track/',views.track,name="track"),

]
