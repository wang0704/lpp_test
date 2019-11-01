# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpp_test', '0005_auto_20191025_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='uhost',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u5220\u9664'),
        ),
    ]
