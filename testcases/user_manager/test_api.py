# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: test_api.py
# @Time : 2022/11/5 15:05
import random
import allure
import pytest
import yaml
from commons.requests_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml


@allure.epic("微信接口项目")
class TestApi:

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=1)
    @allure.description("这是一个获取token的用例")
    @allure.title("这里会被动态标题替换掉")
    def test_get_token(self, base_url):
        urls = base_url + "/cgi-bin/token"
        datas = {
            "grant_type": "client_credential",
            "appid": "wxf393fadf3268a5d5",
            "secret": "e9a29dfa3920020ebee3675bcc9c2cf8"
        }
        res = RequestUtil().send_all_request(method="get", url=urls, params=datas)
        # res = requests.get(url=urls, params=datas)
        result = res.json()
        data_token = {"ACCESS_TOKEN": result["access_token"]}
        write_yaml("extract.yaml", data_token)
        # print(result, type(result))
        assert result['expires_in'] == 7200
        allure.dynamic.title("获取token测试用例")

    @allure.title("选择标签测试用例")
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_select_flag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/get"
        datas = {
            "access_token": read_yaml("extract.yaml", "ACCESS_TOKEN")
        }
        with allure.step("发起请求"):
            res = RequestUtil().send_all_request(method="get", url=urls, params=datas)
            result = res.json()
        with allure.step("打印结果"):
            pass
        print(result, type(result))
        # raise Exception("失败了请检查！")

    @allure.title("编辑标签测试用例")
    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    def test_edit_flag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/update"
        datas = {
            "access_token": read_yaml("extract.yaml", "ACCESS_TOKEN")
        }
        jsons = {"tag": {"id": 134, "name": "广东人" + str(random.randint(1, 999999999))}}
        res = RequestUtil().send_all_request(method="post", url=urls, json=jsons, params=datas)
        result = res.json()
        print(result, type(result))

    @allure.title("删除标签测试用例")
    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    def test_del_flag(self):
        urls = "https://api.weixin.qq.com/cgi-bin/tags/delete"
        datas = {
            "access_token": read_yaml("extract.yaml", "ACCESS_TOKEN")
        }
        jsons = {"tag": {"id": 134}}
        res = RequestUtil().send_all_request(method="post", url=urls, json=jsons, params=datas)
        result = res.json()
        print(result, type(result))
        assert res.json()['errcode'] == 0
        print("删除标签测试用例--断言通过")

    @allure.title("文件上传测试用例")
    @pytest.mark.run(order=5)
    def test_file_upload(self):
        urls = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
        datas = {
            "access_token": read_yaml("extract.yaml", "ACCESS_TOKEN")
        }
        file = {"media": open("D:\\pig.jpg", "rb")}
        res = RequestUtil().send_all_request(method="post", url=urls, files=file, params=datas)
        result = res.json()
        print(result, type(result))

        # print("删除标签测试用例--断言通过")
