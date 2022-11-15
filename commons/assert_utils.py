# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: assert_utils.py
# @Time : 2022/11/11 14:06
import traceback
import jsonpath
from commons.logger_utils import print_log, error_log


def assert_result(expect_result, actual_result, status_code):
    try:
        all_flag = 0
        if expect_result:
            # print(expect_result)
            for expect in expect_result:
                for key, value in expect.items():
                    if key == "codes":
                        print_log("执行状态码断言")
                        flag = codes_assert(value, status_code)
                        all_flag = all_flag + flag
                    elif key == "equals":
                        print_log("执行相等断言")
                        flag = equals_assert(value, actual_result)
                        all_flag = all_flag + flag
                    elif key == "contains":
                        print_log("执行包含断言")
                        flag = contains_assert(value, actual_result)
                        all_flag = all_flag + flag
                    else:
                        print_log("此框架不支持{}断言方式".format(key))
        else:
            all_flag = -1
        return all_flag

    except Exception as e:
        error_log("assert_utils模块assert_result方法报错：%s" % str(traceback.format_exc()))
        raise e


# 状态码断言：
def codes_assert(value, status_code):
    try:
        flag = 0
        for assert_key, assert_value in value.items():
            if assert_key == "status_code":
                if assert_value != status_code:
                    flag = flag + 1
                    print_log("codes断言失败：" + str(assert_key) + "不等于" + str(assert_value) + "")
        return flag
    except Exception as e:
        error_log("assert_utils模块codes_assert方法报错：%s" % str(traceback.format_exc()))
        raise e


def equals_assert(value, actual_result):
    try:
        flag = 0
        for assert_key, assert_value in value.items():
            lists = jsonpath.jsonpath(actual_result, '$..%s' % assert_key)
            # print(lists)
            if lists:
                if assert_value not in lists:
                    flag = flag + 1
                    print_log("equals断言失败：" + str(assert_key) + "不等于" + str(assert_value) + "")
            else:
                flag = flag + 1
                print_log("equals断言失败：返回的结果中没有" + str(assert_key) + "")
        return flag

    except Exception as e:
        error_log("assert_utils模块equals_assert方法报错：%s" % str(traceback.format_exc()))
        raise e


# 包含断言：
def contains_assert(value, actual_result):
    try:
        flag = 0
        if str(value) not in str(actual_result):
            flag = flag + 1
            print_log("contains断言失败：返回的结果中没有" + str(value) + "")
        return flag
    except Exception as e:
        error_log("assert_utils模块contains_assert方法报错：%s" % str(traceback.format_exc()))
        raise e


# 数据库断言：
def database_assert(value, actual_result):
    flag = 0
    print("------------------------------------------------", value, actual_result)
    return flag
