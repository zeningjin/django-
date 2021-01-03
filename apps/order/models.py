from django.db import models
from apps.user.models import *
from db.base_model import BaseModel
from apps.goods.models import *


class Order(BaseModel):
    ORDER_CHOICES = (
        (0, '待付款'),
        (1, '待发货'),
        (2, '已收货'),
        (3, '已完成'),
    )
    user = models.ForeignKey(User, verbose_name='所属账号', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name='地址', on_delete=models.CASCADE)
    number = models.CharField(max_length=256, verbose_name='订单编号')
    order_type = models.IntegerField(verbose_name='订单类型', choices=ORDER_CHOICES, default=1)

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'ct_order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderGoods(BaseModel):
    order = models.ForeignKey(Order, verbose_name='订单', on_delete=models.CASCADE)
    antique = models.ForeignKey(GoodsSize, verbose_name='购买商品', on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='购买数量', default=1)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'ct_order_goods'
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name


class LogisticsInfo(BaseModel):
    order = models.ForeignKey(Order, verbose_name='订单', on_delete=models.CASCADE)
    json_col = models.TextField(blank=True, null=True, verbose_name='物流信息')

    def __str__(self):
        return self.json_col

    class Meta:
        verbose_name = '物流信息'
        verbose_name_plural = verbose_name
        db_table = 'ct_logistics'


class Phone(models.Model):
    phone = models.CharField(verbose_name="手机号", max_length=20)
    code = models.CharField(verbose_name="验证码", max_length=20)

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'ct_login_phone'
        verbose_name = '手机验证'
        verbose_name_plural = verbose_name
