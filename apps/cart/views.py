from django.shortcuts import render, redirect, reverse
from apps.cart.models import *
from apps.user.models import *
from django.core import serializers
from django.http import JsonResponse


def shop_cart(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect(reverse('user:login'))
        goods = CartInfo.objects.filter(user_id=user_id)
        price = 0
        for g in goods:
            price += g.size.goodsSku.goodsSpu.price * g.count
        addr = Address.objects.filter(user_id=user_id)
        context = {
            'goods': goods,
            'price': price,
            'addr': addr
        }
        return render(request, 'cart/shopcart.html', context=context)


def add_cart(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        print(user_id)
        size_id = request.POST.get('size_id')
        print(size_id)
        num = request.POST.get('num')
        print(num)
        CartInfo.objects.create(
            user_id=user_id,
            size_id=size_id,
            count=num
        )
        return JsonResponse({'mes':'ok'}, safe=False)


def del_cart(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        CartInfo.objects.filter(id=cart_id).delete()
        return redirect(reverse('cart:cart'))


def add_goods_quantity(request, cart_id):
    cart = CartInfo.objects.filter(id=cart_id)
    cart.update(count=cart.first().count+1)
    return redirect(reverse('cart:cart'))


def del_goods_quantity(request, cart_id):
    cart = CartInfo.objects.filter(id=cart_id)
    if cart.first().count == 1:
        return redirect(reverse('cart:cart'))
    cart.update(count=cart.first().count-1)
    return redirect(reverse('cart:cart'))