# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: conftest.py
# @Time : 2022/11/8 16:51
import pytest
from commons.yaml_util import clear_yaml


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    clear_yaml("extract.yaml")
