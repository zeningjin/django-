from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField


class TypeInfo(BaseModel):
    title = models.CharField(max_length=20, verbose_name="分类")
    type = models.ForeignKey('self', verbose_name='关联父分类', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ct_goods_type'
        verbose_name = "商品类型"
        verbose_name_plural = verbose_name


class GoodsSPU(models.Model):
    status_choices = (
        (0, '下线'),
        (1, '上线'),
    )
    title = models.CharField(max_length=20, verbose_name="商品名称", unique=True)
    pic = models.ImageField(verbose_name='商品首图', upload_to='images/goods/spu/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    views = models.IntegerField(verbose_name="浏览数", default=0)
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='商品状态')
    type = models.ForeignKey(TypeInfo, on_delete=models.CASCADE, verbose_name="分类")
    synopsis = models.CharField(max_length=2000, verbose_name="简介")
    content = HTMLField(max_length=2000, verbose_name="详情")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ct_goods_spu'
        verbose_name = "商品spu"
        verbose_name_plural = verbose_name


class GoodsSKU(BaseModel):
    goodsSpu = models.ForeignKey(GoodsSPU, verbose_name='商品SPU', on_delete=models.CASCADE)
    pic = models.ImageField(verbose_name='商品首图', upload_to='images/goods/sku/', null=True, blank=True)
    stock = models.IntegerField(verbose_name='库存', default=0)
    sales = models.IntegerField(default=0, verbose_name='商品销量')
    color = models.CharField(max_length=64, verbose_name="颜色")

    def __str__(self):
        return self.goodsSpu.title

    class Meta:
        db_table = 'ct_goods_sku'
        verbose_name = "商品sku"
        verbose_name_plural = verbose_name


class GoodsSize(models.Model):
    size = models.CharField(max_length=64, verbose_name="尺寸")
    goodsSku = models.ForeignKey(GoodsSKU, verbose_name='商品SKU', on_delete=models.CASCADE)

    def __str__(self):
        return self.goodsSku.goodsSpu.title

    class Meta:
        db_table = 'ct_goods_size'
        verbose_name = "商品尺寸"
        verbose_name_plural = verbose_name


class IndexGoodsBanner(BaseModel):
    sku = models.ForeignKey(GoodsSPU, verbose_name='商品', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/goods/banner/', verbose_name='轮播图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'ct_index_banner'
        verbose_name = '首页轮播商品'
        verbose_name_plural = verbose_name
