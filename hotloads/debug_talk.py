# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: debug_talk.py
# @Time : 2022/11/11 0:12
import os
import random
import yaml


class DebugTalk:
    def get_random(self, min_num, max_num):
        return random.randint(int(min_num), int(max_num))

    def read_extract(self, key):
        with open(os.getcwd() + "/" + "/extract.yaml", mode="r", encoding="utf-8") as f:
            result = yaml.load(stream=f, Loader=yaml.FullLoader)
            return result[key]



