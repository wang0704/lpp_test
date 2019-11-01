# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpp_test', '0002_auto_20191024_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='id', primary_key=True),
        ),
        migrations.AlterField(
            model_name='uhost',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='id', primary_key=True),
        ),
    ]
