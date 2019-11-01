# -*- coding: utf-8 -*-
from blueking.component.client import ComponentClient
from conf.default import APP_ID, APP_TOKEN
from models import Business,UHost

app_code = APP_ID
app_secret = APP_TOKEN
# 用户信息
common_args = {'bk_token': 'SgNRKBhFN4ImtGd28dNkEzMb_91MetH1Fgs0TWosnRo'}

client = ComponentClient(
         app_code=app_code,
         app_secret=app_secret,
         common_args=common_args
     )


def init_business(total=10, start=0):
    client.cc.search_business.path = "http://paas.bk.com:80/" + client.cc.search_business.path
    kwargs = {"page": {"total": total, "start": start}}
    result = client.cc.search_business(kwargs)
    count = result.get("data").get("count", 0) if result.get("data") else None
    for key in result.get("data").get("info"):
        print key
    if count == total:
        init_business(total=total, start=start+count)


def init_host(total=10, start=0):
    client.cc.search_host.path = "http://paas.bk.com:80/" + client.cc.search_host.path
    kwargs = {"page": {"total": total, "start": start}}
    result = client.cc.search_business(kwargs)


if __name__ == "__main__":
    init_business(total=10, start=0)