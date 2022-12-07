from django.urls import path
from hairoil import views
urlpatterns = [

    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('checkout/',views.checkout),
    path('shop/',views.shop),
    path('news/',views.news),
    path('cart/',views.cart),
    path('singleproduct/',views.singleproduct),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('adminlogin/',views.adminlogin),
    path('adlogout/',views.adlogout),
    path('adminindex/',views.adminindex),
    path('blocks/',views.blocks),
    path('cards/',views.cards),
    path('carousels/',views.carousels),
    path('people/',views.people),
    path('forms/',views.forms),
    path('pricing/',views.pricing),
    path('addproduct/',views.addproduct),
    path('productupdate/',views.productupdate),
    path('addcart/',views.addcart),
    path('cart/',views.cart),
    path('deleteitem/',views.deleteitem),
    path('cartupdate/',views.cartupdate),
    

]