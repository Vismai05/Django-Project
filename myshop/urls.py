from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('product/<int:id>',views.product,name="products"),
    path('search/',views.search,name="search"),
    path('about',views.about,name="aboutus"),
    path('contact',views.Contact,name="contactus"),
    path('tracker',views.tracker,name="trackingprd"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('login',views.lgnpage,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.lgoutpage,name="logout")
]