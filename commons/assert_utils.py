# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: assert_utils.py
# @Time : 2022/11/11 14:06
import jsonpath


def assert_result(expect_result, actual_result, status_code):
    all_flag = 0
    for expect in expect_result:
        for key, value in expect.items():
            if key == "codes":
                print("状态码断言")
                flag = codes_assert(value, status_code)
                all_flag = all_flag + flag
            elif key == "equals":
                print("相等断言")
                flag = equals_assert(value, actual_result)
                all_flag = all_flag + flag
            elif key == "contains":
                print("包含断言")
                flag = contains_assert(value, actual_result)
                all_flag = all_flag + flag
            else:
                print("此框架不支持{}断言方式".format(key))
    return all_flag


# 状态码断言：
def codes_assert(value, status_code):
    flag = 0
    for assert_key, assert_value in value.items():
        if assert_key == "status_code":
            if assert_value != status_code:
                flag = flag + 1
                print("codes断言失败：" + str(assert_key) + "不等于" + str(assert_value) + "")
    return flag


def equals_assert(value, actual_result):
    flag = 0
    for assert_key, assert_value in value.items():
        print("assert_key:%s" % assert_key)
        print("assert_value:%s" % assert_value)
        lists = jsonpath.jsonpath(actual_result, '$..%s' % assert_key)
        print(lists)
        if lists:
            if assert_value not in lists:
                flag = flag + 1
                print("equals断言失败：" + str(assert_key) + "不等于" + str(assert_value) + "")
        else:
            flag = flag + 1
            print("equals断言失败：返回的结果中没有" + str(assert_key) + "")
    return flag


# 包含断言：
def contains_assert(value, actual_result):
    flag = 0
    if str(value) not in str(actual_result):
        flag = flag + 1
        print("contains断言失败：返回的结果中没有" + str(value) + "")
    return flag


# 数据库断言：
def database_assert(value, actual_result):
    flag = 0
    print("------------------------------------------------",value, actual_result)
    return flag
