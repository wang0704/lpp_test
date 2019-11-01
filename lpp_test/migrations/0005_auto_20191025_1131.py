# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpp_test', '0004_uhost_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uhost',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u4e3b\u673a\u540d\u79f0'),
        ),
    ]
