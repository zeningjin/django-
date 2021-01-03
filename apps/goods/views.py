import json
from django.shortcuts import render, redirect, reverse
from apps.goods.models import *
from apps.user.models import *
from django.core import serializers
from django.http import JsonResponse


def index(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(reverse('user:login'))
    type_info = TypeInfo.objects.all()
    content = GoodsSPU.objects.all()
    hot = GoodsSPU.objects.all().order_by('-views')[0: 2]
    new = GoodsSPU.objects.all().order_by('-id')[0: 5]
    male = GoodsSPU.objects.filter(type_id=1).order_by('-id')[0: 5]
    female = GoodsSPU.objects.filter(type_id=3).order_by('-id')[0: 5]
    context = {
        'hot': hot,
        'type_info': type_info,
        'content': content,
        'today': content.order_by('-views')[0: 4],
        'today1': content.order_by('-views')[4: 8],
        'new': new,
        'male': male,
        'female': female
    }
    return render(request, 'goods/index.html', context=context)


def goods_search(request):
    search1 = request.GET.get('search')
    content = GoodsSPU.objects.filter(title__icontains=search1).order_by('-id')
    context = {'content': content}
    return render(request, 'goods/goods_search.html', context=context)


def goods_all(request, type_id=0):
    type_info = TypeInfo.objects.all()
    context = {'type_info': type_info, 'type_id': type_id}
    return render(request, 'goods/goods_all.html', context=context)


def goods_all_api(request, type_id='0'):
    if type_id == '01':
        content = GoodsSPU.objects.all().order_by('price')
    elif type_id == '02':
        content = GoodsSPU.objects.all().order_by('-id')
    elif type_id == '0':
        content = GoodsSPU.objects.all()
    else:
        content = GoodsSPU.objects.filter(type_id=type_id)
    json_data = serializers.serialize('json', content)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)


def goods_detail(request, goods_id):
    gb = GoodsBrowser.objects.filter(good_id=goods_id)
    if not gb:
        user_id = request.session.get('user_id')
        GoodsBrowser.objects.create(good_id=goods_id, user_id=user_id)
    goods = GoodsSPU.objects.filter(id=goods_id).first()
    context = {'goods': goods}
    return render(request, 'goods/goods_detail.html', context)


def api_goods_size(request):
    sku_id = request.GET.get('sku_id')
    content = GoodsSize.objects.filter(goodsSku_id=sku_id)
    json_data = serializers.serialize('json', content)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)


def goods_browser(request):
    user_id = request.session.get('user_id')
    goods = GoodsBrowser.objects.filter(user_id=user_id)
    context = {
        'goods': goods
    }
    return render(request, 'goods/goods_browser.html', context)


def promotion(request):
    goods = GoodsSPU.objects.filter(synopsis="促销")
    context = {
        'goods': goods
    }
    return render(request, 'goods/promotion.html', context)


def must_seize(request):
    goods = GoodsBrowser.objects.filter(synopsis="必抢")
    context = {
        'goods': goods
    }
    return render(request, 'goods/must_seize.html', context)
