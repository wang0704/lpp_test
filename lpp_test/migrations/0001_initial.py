# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='\u529f\u80fdcode', primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u529f\u80fd\u540d\u79f0')),
            ],
        ),
    ]
