# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: test_weixin.py
# @Time : 2022/11/5 15:05
import allure
import pytest
from commons.ddt_utils import read_case_yaml
from commons.logger_utils import print_log
from commons.requests_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml
from hotloads.debug_talk import DebugTalk


@allure.epic("微信接口项目")
class TestApi:

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=1)
    @allure.description("这是一个获取token的用例")
    @allure.title("获取token测试用例")
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/get_token.yaml"))
    def test_get_token(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.title("选择标签测试用例")
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/select_flag.yaml"))
    def test_select_flag(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.title("编辑标签测试用例")
    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/edit_flag.yaml"))
    def test_edit_flag(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.title("删除标签测试用例")
    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/delete_flag.yaml"))
    def test_del_flag(self,caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.title("文件上传测试用例")
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/files_upload.yaml"))
    def test_file_upload(self,caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.title("md5加密接口测试用例")
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/md5_case.yaml"))
    def test_md5_login(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.title("Base64加密接口测试用例")
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/bs64_case.yaml"))
    def test_bs64_login(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.title("RSA加密接口测试用例")
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/rsa_case.yaml"))
    def test_rsa_login(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.title("sign接口测试用例")
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/sign.yaml"))
    def test_sign(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)


    # @allure.title("重置API配额方法")
    # @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/clear_api_quota.yaml"))
    # def clear_api_quota(self, caseinfo):
    #     RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)