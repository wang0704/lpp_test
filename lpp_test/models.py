# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(u"功能code", primary_key=True)
    name = models.CharField(u"功能名称", max_length=64)

    def __unicode__(self):
        return self.id