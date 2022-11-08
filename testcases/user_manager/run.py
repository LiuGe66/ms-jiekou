# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: run.py
# @Time : 2022/11/5 16:15
import os
from time import sleep

import pytest

if __name__ == '__main__':
    pytest.main()
    sleep(3)
    os.system("allure generate ./temps -o ./report --clean report")
