from django.urls import path
from apps.cart.views import *

app_name = 'cart'

urlpatterns = [
    path('cart/', shop_cart, name='cart'),
    path('api/add/cart/', add_cart),
    path('cart/del/', del_cart, name='del_cart'),
    path('cart/del/quantity/<int:cart_id>/', del_goods_quantity, name='del_quantity'),
    path('cart/add/quantity/<int:cart_id>/', add_goods_quantity, name='add_quantity'),

]
