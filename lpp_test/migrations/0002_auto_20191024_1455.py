# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpp_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='id', primary_key=True)),
                ('bk_biz_id', models.IntegerField(verbose_name='bk_biz_id')),
                ('bk_biz_name', models.CharField(max_length=32, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='UHost',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='id', primary_key=True)),
                ('ip', models.CharField(max_length=32, verbose_name='\u4e3b\u673aIP')),
                ('business', models.CharField(max_length=128, verbose_name='\u6240\u5c5e\u4e1a\u52a1')),
                ('area', models.CharField(max_length=128, verbose_name='\u4e91\u533a\u57df')),
                ('op_system', models.CharField(max_length=128, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
