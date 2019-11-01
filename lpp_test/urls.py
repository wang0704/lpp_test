# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.conf.urls import patterns

from lpp_test import views

urlpatterns = patterns(
    'lpp_test.views',
    # 定义URL
    (r'^$', 'hello'),
    (r'^test$', 'test'),
    (r'^init_business$', 'init_business'),
    (r'^init_host$', 'init_host'),
    (r'^create_business$', 'create_business'),
    (r'^delete_business$', 'delete_business'),
    (r'^search_host$', 'search_host'),
    (r'^delete_host', 'delete_host')
)
