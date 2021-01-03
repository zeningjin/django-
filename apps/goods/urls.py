from django.contrib import admin
from django.urls import path
from apps.goods.views import *

app_name = 'goods'

urlpatterns = [
    path('index/', index, name='index'),
    path('goods/search/', goods_search, name='goods_search'),
    path('goods/all/', goods_all, name='goods_all'),
    path('goods/all/<str:type_id>/', goods_all, name='goods_all'),
    path('api/goods/all/', goods_all_api,),
    path('api/goods/all/<str:type_id>/', goods_all_api,),
    path('goods/detail/<int:goods_id>/', goods_detail, name='goods_detail'),
    path('api/goods/detail/size/', api_goods_size),
    path('goods/browser/', goods_browser, name='goods_browser'),
    path('promotion/', promotion, name='promotion'),
    path('must_seize/', must_seize, name='must_seize'),
]
