#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from time import sleep
import pytest


if __name__ == '__main__':
    pytest.main()
    sleep(3)
    os.system("allure generate ./temps -o ./reports --clean reports")
    os.system('allure open report -p 9099')
