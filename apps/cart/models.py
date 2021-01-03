from django.db import models
from apps.user.models import User
from apps.goods.models import GoodsSize


class CartInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    size = models.ForeignKey(GoodsSize, on_delete=models.CASCADE, verbose_name="商品")
    count = models.IntegerField(verbose_name="购买数量", default=0)

    class Meta:
        db_table = 'ct_cart'
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name + '的购物车'
