from django.db import models
from db.base_model import BaseModel
from apps.goods.models import GoodsSPU


class User(BaseModel):
    name = models.CharField(max_length=20, verbose_name="用户名", unique=True)
    pwd = models.CharField(max_length=40, verbose_name="用户密码", blank=False)
    phone = models.CharField(max_length=11, default="", verbose_name="手机号")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ct_user'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class Address(BaseModel):
    user = models.ForeignKey(User, verbose_name='所属用户', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    address = models.CharField(max_length=100, default="", verbose_name="地址")
    zip_code = models.CharField(max_length=12, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=20, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'ct_user_address'
        verbose_name = "用户地址"
        verbose_name_plural = verbose_name


class GoodsBrowser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户id")
    good = models.ForeignKey(GoodsSPU, on_delete=models.CASCADE, verbose_name="商品id")

    def __str__(self):
        return "{0}浏览记录{1}".format(self.user.name, self.good.title)

    class Meta:
        db_table = 'ct_user_goods_browser'
        verbose_name = "用户浏览记录"
        verbose_name_plural = verbose_name
