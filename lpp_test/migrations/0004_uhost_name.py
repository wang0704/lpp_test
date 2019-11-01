# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpp_test', '0003_auto_20191024_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='uhost',
            name='name',
            field=models.CharField(default=b'', max_length=128, verbose_name='\u4e3b\u673a\u540d\u79f0'),
        ),
    ]
