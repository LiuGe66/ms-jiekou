# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: ddt_utils.py
# @Time : 2022/11/11 21:26
import json

import yaml
from commons.yaml_util import get_object_path


# 读取测试用例
def read_case_yaml(yaml_path):
    with open(get_object_path() + "/" + yaml_path, mode="r", encoding="utf-8") as f:
        caseinfo = yaml.load(stream=f, Loader=yaml.FullLoader)
        if len(caseinfo) >= 2:  # 表示通过复制内容实现数据驱动
            return caseinfo
        else:
            if "parameterize" in dict(*caseinfo).keys():
                # 代表需要做解析
                new_caseinfo = parameterize_ddt(*caseinfo)
                pass
                return new_caseinfo
            else:
                return caseinfo


# 解析测试用例
def parameterize_ddt(caseinfo):
    caseinfo_str = json.dumps(caseinfo)
    data_list = caseinfo["parameterize"]
    # 规范数据驱动的写法
    length_success = True
    key_length = len(caseinfo["parameterize"][0])
    # 循环数据
    for param in caseinfo["parameterize"]:
        if len(param) != key_length:
            length_success = False
            print("name为：'{}'的这条数据有误，请检查。".format(param[0]))
            print('数据规范发现异常：key与value的数量不对应')
            continue
    new_caseinfo = []
    if length_success:
        for x in range(1, len(data_list)):
            # print("x=======%s" % x)
            print(caseinfo_str)
            raw_caseinfo = caseinfo_str
            for y in range(0, len(data_list[x])):
                # print("y=======%s" % y, data_list[x][y])
                raw_caseinfo = raw_caseinfo.replace("$ddt{" + data_list[0][y] + "}", str(data_list[x][y]))
            new_caseinfo.append(json.loads(raw_caseinfo))
        print("999999999999999999", new_caseinfo)

    return new_caseinfo
