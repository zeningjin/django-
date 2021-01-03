from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)

    class Meta:
        abstract = True
