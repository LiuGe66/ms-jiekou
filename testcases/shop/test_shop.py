# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: test_weixin.py
# @Time : 2022/11/5 15:05
import time

import allure
import pytest
from commons.ddt_utils import read_case_yaml
from commons.requests_util import RequestUtil
from hotloads.debug_talk import DebugTalk


@allure.epic("商城接口项目")
class TestApi:

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=1)
    @allure.description("这是一个获取token的用例")
    @allure.title("商城登录测试用例")
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/shop/shop_login.yaml"))
    def test_shop_login(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=2)
    @allure.title("加入购物车测试用例")
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/shop/cart_save.yaml"))
    def test_cart_save(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)
