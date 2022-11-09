# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: test_weixin.py
# @Time : 2022/11/5 15:05
import random
import re
import allure
import pytest
from commons.requests_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml, read_case_yaml


@allure.epic("微信接口项目")
class TestApi:

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=1)
    @allure.description("这是一个获取token的用例")
    @allure.title("这里会被动态标题替换掉")
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/get_token.yaml"))
    def test_get_token(self, caseinfo):
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        header = caseinfo['request']['headers']
        params = caseinfo['request']['params']
        validate = caseinfo['validate']
        res = RequestUtil().send_all_request(method="get", url=url, params=params)
        result = res.json()
        data_token = {"ACCESS_TOKEN": result["access_token"]}
        write_yaml("extract.yaml", data_token)
        assert result['expires_in'] == 7200
        allure.dynamic.title("获取token测试用例")


    @allure.title("选择标签测试用例")
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/select_flag.yaml"))
    def test_select_flag(self, caseinfo):
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        header = caseinfo['request']['headers']
        params = caseinfo['request']['params']
        for key, value in params.items():
            params["access_token"] = read_yaml("extract.yaml", "ACCESS_TOKEN")
        validate = caseinfo["validate"]
        res = RequestUtil().send_all_request(method=method, url=url, params=params)
        result = res.json()
        print(result, type(result))

    @allure.title("编辑标签测试用例")
    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/edit_flag.yaml"))
    def test_edit_flag(self, caseinfo):
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        header = caseinfo['request']['headers']
        params = caseinfo['request']['params']
        for key, value in params.items():
            params["access_token"] = read_yaml("extract.yaml", "ACCESS_TOKEN")
        json = caseinfo['request']['json']
        validate = caseinfo["validate"]
        res = RequestUtil().send_all_request(method="post", url=url, json=json, params=params)
        result = res.json()
        print(result, type(result))

    @allure.title("删除标签测试用例")
    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/delete_flag.yaml"))
    def test_del_flag(self,caseinfo):
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        header = caseinfo['request']['headers']
        params = caseinfo['request']['params']
        for key, value in params.items():
            params["access_token"] = read_yaml("extract.yaml", "ACCESS_TOKEN")
        json = caseinfo['request']['json']
        validate = caseinfo["validate"]
        res = RequestUtil().send_all_request(method="post", url=url, json=json, params=params)
        result = res.json()
        print(result, type(result))
        assert res.json()['errcode'] == 0
        print("删除标签测试用例--断言通过")

    @allure.title("文件上传测试用例")
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/files_upload.yaml"))
    def test_file_upload(self,caseinfo):
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        header = caseinfo['request']['headers']
        params = caseinfo['request']['params']
        for key, value in params.items():
            params["access_token"] = read_yaml("extract.yaml", "ACCESS_TOKEN")
        json = caseinfo['request']['json']
        files = caseinfo['request']['files']
        for key, value in files.items():
            files[key] = open(value, "rb")
        validate = caseinfo["validate"]
        res = RequestUtil().send_all_request(method="post", url=url, files=files, params=params)
        result = res.json()
        print(result, type(result))
    #
    # @allure.title("访问论坛首页")
    # @pytest.mark.run(order=6)
    # def test_index(self):
    #     urls = "http://47.107.116.139/phpwind/"
    #     res = RequestUtil().send_all_request(method="get", url=urls)
    #     result = res.text
    #     data_token = {"csrf_token": re.search('name="csrf_token" value="(.*?)"', result).group(1)}
    #     write_yaml("extract.yaml", data_token)
    #     # TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"', result).group(1)
    #
    # @allure.title("登录论坛")
    # @pytest.mark.run(order=7)
    # def test_login(self):
    #     urls = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
    #     header = {
    #         "Accept": "application/json, text/javascript, /; q=0.01",
    #         "X-Requested-With": "XMLHttpRequest"
    #     }
    #     datas = {
    #         "username": "liuge",
    #         "password": "2066Sixy",
    #         "csrf_token": read_yaml("extract.yaml", "csrf_token"),
    #         "backurl": "http://47.107.116.139/phpwind/",
    #         "invite": ""
    #     }
    #     res = RequestUtil().send_all_request(method="post", url=urls, headers=header, data=datas)
    #     result = res.text
    #     assert 'success' in result
