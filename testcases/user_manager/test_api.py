# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: test_api.py
# @Time : 2022/11/5 15:05
import pytest
import requests

class TestApi:
    access_token = ""

    @pytest.mark.run(order=1)
    def test_get_token(self, base_url):
        urls = base_url+"/cgi-bin/token"
        datas = {
            "grant_type": "client_credential",
            "appid": "wxf393fadf3268a5d5",
            "secret": "e9a29dfa3920020ebee3675bcc9c2cf8"
        }
        res = requests.get(url=urls, params=datas)
        result = res.json()
        TestApi.access_token = result["access_token"]
        # print(result, type(result))

    @pytest.mark.smoke
    def test_select_flag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/get"
        datas = {
            "access_token": TestApi.access_token
        }
        res = requests.get(url=urls, params=datas)
        result = res.json()
        print(result, type(result))
        # raise Exception("失败了请检查！")

    def test_test(self):
        print("用例3")
