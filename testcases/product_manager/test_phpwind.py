# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: test_phpwind.py
# @Time : 2022/11/5 15:05
import random
import re
import allure
import pytest
from commons.requests_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml, read_case_yaml


# @allure.epic("论坛项目")
# class TestApiBbs:
#
#     @allure.title("访问论坛首页")
#     @pytest.mark.run(order=6)
#     @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/product_manager/index.yaml"))
#     def test_index(self, caseinfo):
#         RequestUtil().standard_yaml_testcase(caseinfo)
#
#     @allure.title("登录论坛")
#     @pytest.mark.run(order=7)
#     @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/product_manager/login.yaml"))
#     def test_login(self, caseinfo):
#         RequestUtil().standard_yaml_testcase(caseinfo)
