# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: test_weixin.py
# @Time : 2022/11/5 15:05
import allure
import pytest
from commons.requests_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml, read_case_yaml
from hotloads.debug_talk import DebugTalk


@allure.epic("微信接口项目")
class TestApi:

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=1)
    @allure.description("这是一个获取token的用例")
    @allure.title("这里会被动态标题替换掉")
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/get_token.yaml"))
    def test_get_token(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)

    @allure.title("选择标签测试用例")
    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/select_flag.yaml"))
    def test_select_flag(self, caseinfo):
        RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)
    #
    # @allure.title("编辑标签测试用例")
    # @pytest.mark.run(order=3)
    # @pytest.mark.smoke
    # @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/edit_flag.yaml"))
    # def test_edit_flag(self, caseinfo):
    #     RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)
    #
    # @allure.title("删除标签测试用例")
    # @pytest.mark.run(order=4)
    # @pytest.mark.smoke
    # @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/delete_flag.yaml"))
    # def test_del_flag(self,caseinfo):
    #     RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)
    #
    # @allure.title("文件上传测试用例")
    # @pytest.mark.run(order=5)
    # @pytest.mark.parametrize("caseinfo", read_case_yaml("testcases/user_manager/files_upload.yaml"))
    # def test_file_upload(self,caseinfo):
    #     RequestUtil(DebugTalk).standard_yaml_testcase(caseinfo)
