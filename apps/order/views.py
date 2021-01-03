from django.shortcuts import render, redirect, reverse
from apps.cart.models import *
from apps.order.models import *


def orders(request):
    user_id = request.session.get('user_id')
    if request.method == "GET":
        order = Order.objects.filter(user_id=user_id)
        context = {
            'order': order,
        }
        return render(request, 'order.html', context)

    elif request.method == "POST":
        addr = request.POST.get('address')
        cart = CartInfo.objects.filter(user_id=user_id)
        order = Order.objects.create(
            user_id=user_id,
            address_id=addr,
            number='test',
        )
        for g in cart:
            OrderGoods.objects.create(
                order_id=order.id,
                antique_id=g.size_id,
                number=g.count
            )
        cart.delete()
        return redirect(reverse('order:orders'))