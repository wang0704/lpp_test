# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.


class Business(models.Model):
    id = models.AutoField(u'id', primary_key=True,)
    bk_biz_id = models.IntegerField(u'bk_biz_id')
    bk_biz_name = models.CharField(u'name', max_length=32)


class UHost(models.Model):
    id = models.AutoField(u'id', primary_key=True)
    ip = models.CharField(u'主机IP', null=False,max_length=32)
    name = models.CharField(u'主机名称',max_length=128)
    business = models.CharField(u'所属业务', max_length=128)
    area = models.CharField(u'云区域', max_length=128)
    op_system = models.CharField(u'操作系统', max_length=128)
    is_delete = models.BooleanField(u'是否删除', default=True)
