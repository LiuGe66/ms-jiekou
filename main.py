# -*- coding: utf-8 -*-
# Author:liu_ge
# @FileName: run.py
# @Time : 2022/11/5 16:15
import os
from time import sleep
import pytest

from commons.yaml_util import read_yaml

if __name__ == '__main__':
    pytest.main()
    sleep(3)
    os.system("allure generate ./temps -o ./reports --clean reports")
