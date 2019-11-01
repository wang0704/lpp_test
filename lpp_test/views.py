# coding=utf-8
import json
import math

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from common.mymako import render_mako_context
from blueking.component.shortcuts import get_client_by_request
from conf.default import APP_ID, TIME_ZONE
from models import Business, UHost


def hello(request):
    # context = {'hello': 'Hello World!'}
    page_now = int(request.GET.get('page_num', 1))
    count = UHost.objects.filter(is_delete=False).count()
    page_size = 2
    page_all = int(math.ceil(float(count) / float(page_size)))
    start = 0 if page_now <= 1 else (page_now - 1) * page_size
    hosts = UHost.objects.filter(is_delete=False).all()[start:start + page_size]

    return render_mako_context(request, '/lpp_test/hello.html', {'hosts': hosts,
                                                                 'count': count,
                                                                 'page_size': page_size,
                                                                 'page_now': page_now,
                                                                 'page_all': page_all,
                                                                 }
                               )


def delete_host(request):
    ip = request.POST.get('ip')
    try:
        obj = UHost.objects.filter(ip=ip).first()
        obj.is_delete = True
        obj.save()
    except Exception as e:
        raise e
    return HttpResponse(json.dumps({"ip": ip, "result": True}), content_type="application/json")


def test(request):
    client = get_client_by_request(request)
    kwargs = {}
    result = client.cc.search_business(kwargs)
    return render_mako_context(request, '/lpp_test/test.html', result)


def create_business(request, bk_zip_name=APP_ID):
    client = get_client_by_request(request)
    kwargs = {"data": {"bk_biz_name": bk_zip_name,
                       "bk_biz_maintainer": request.user.username,
                       "bk_biz_productor": request.user.username,
                       "bk_biz_developer": request.user.username,
                       "bk_biz_tester": request.user.username,
                       "time_zone": TIME_ZONE}}
    result = client.cc.create_business(kwargs)
    if result.get('result') is True:
        Business.objects.create(bk_biz_id=request.get('data').get('bk_biz_id'), bk_biz_name=bk_zip_name)
        return HttpResponse(u"<p>业务添加成功！</p>")
    else:
        return HttpResponse(u"<p>业务添加失败！</p>")


def delete_business(request, bk_biz_id=4):
    client = get_client_by_request(request)
    kwargs = {"bk_biz_id": bk_biz_id}
    result = client.cc.delete_business(kwargs)
    print result
    if result.get('result') is True:
        business = Business.objects.get(bk_biz_id=bk_biz_id)
        business.delete()
        return HttpResponse(u"<p>业务删除成功！</p>")
    else:
        return HttpResponse(u"<p>业务删除失败！</p>")


def search_host(request):
    result = UHost.objects.filter(is_delete=True).all()[0:10]
    if result:
        data = []
        for key in result:
            data.append({"ip": key.ip})
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return HttpResponse(u"<p>主机查询错误！</p>")


def init_business(request, total=10, start=0):
    client = get_client_by_request(request)
    kwargs = {}
    result = client.cc.search_business(kwargs)
    count = result.get("data").get("count", 0) if result.get("data") else None
    for key in result.get("data").get("info"):
        business = Business.objects.filter(bk_biz_id=key.get("bk_biz_id"))
        if business:
            continue
        Business.objects.create(bk_biz_id=key.get("bk_biz_id"), bk_biz_name=key.get("bk_biz_name"))

    if count == total:
        init_business(request=request, total=total, start=start + count)
    return HttpResponse(u"<p>数据添加成功1！</p>")


def init_host(request, total=1, start=0):
    client = get_client_by_request(request)
    kwargs = {"condition": [{
        "bk_obj_id": "biz",
        "fields": ['bk_biz_id'],
        "condition": []
    },{
        "bk_obj_id": "host",
        "fields": [],
        "condition": [
            {
                "field": "bk_host_innerip",
                "operator": "$eq",
                "value": '172.16.150.35'
            }
        ]
    }
    ]}
    result = client.cc.search_host(kwargs)
    count = result.get("data").get("count", 0) if result.get("data") else None
    print result
    # for key in result.get("data").get("info"):
    #     bk_host_innerip = key.get('host').get('bk_host_innerip')
    #     host = UHost.objects.filter(ip=bk_host_innerip)
    #     if host:
    #         continue
    #     UHost.objects.create(ip=key.get('host').get('bk_host_innerip'),
    #                          name=key.get('host').get('bk_host_name'),
    #                          op_system=key.get('host').get('bk_os_name'),
    #                          area=key.get('host').get('bk_cloud_id')[0].get('bk_inst_name'),
    #                          business=key.get('biz')[0].get("bk_biz_name"))
    # if count == total:
    #     init_business(request=request, total=total, start=start + count)
    return HttpResponse(u"<p>数据添加成功1！</p>")
