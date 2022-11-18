# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: conftest.py
# @Time : 2022/11/8 16:51
import os
import shutil
import pytest
from commons.logger_utils import print_log
from commons.yaml_util import clear_yaml


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_yaml("extract.yaml")


@pytest.fixture(scope="session", autouse=True)
def clear_logs():
    path = os.getcwd()
    files_count = len(os.listdir(path + "\\logs\\"))
    num = 10
    if files_count >= num:
        # 先强制删除指定目录
        shutil.rmtree(path + "\\logs\\")
        # 再新建一个同名目录
        os.mkdir(path + "\\logs\\")
        print_log("log数量超过{}条，日志目录已清空".format(num))


if __name__ == '__main__':
    clear_logs()