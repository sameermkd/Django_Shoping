from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("cart", views.cart, name="cart"),
    path('add/<int:id>/', views.cart_add, name='cart_add'),
    path('item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
]
