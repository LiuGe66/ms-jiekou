# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: assert_utils.py
# @Time : 2022/11/11 14:06
import traceback
import jsonpath
from commons.database_utils import DataBaseUtil
from commons.logger_utils import print_log, error_log


def assert_result(expect_result, actual_result, status_code):
    try:
        all_flag = 0
        if expect_result:
            for expect in expect_result:
                for key, value in expect.items():
                    if key == "codes":
                        flag = codes_assert(value, status_code)
                        all_flag = all_flag + flag
                    elif key == "equals":
                        flag = equals_assert(value, actual_result)
                        all_flag = all_flag + flag
                    elif key == "contains":
                        flag = contains_assert(value, actual_result)
                        all_flag = all_flag + flag
                    elif key == "db_equals":
                        flag = database_assert(value, actual_result)
                        all_flag = all_flag + flag
                    else:
                        print_log("此框架不支持{}断言方式".format(key))
        else:
            all_flag = -1  # 无断言设置标记位
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
                else:
                    print_log("codes断言成功")
        return flag
    except Exception as e:
        error_log("assert_utils模块codes_assert方法报错：%s" % str(traceback.format_exc()))
        raise e


def equals_assert(value, actual_result):
    try:
        flag = 0
        for assert_key, assert_value in value.items():
            lists = jsonpath.jsonpath(actual_result, '$..%s' % assert_key)
            if lists:
                if assert_value not in lists:
                    flag = flag + 1
                    print_log("equals断言失败：" + str(assert_key) + "不等于" + str(assert_value) + "")
                else:
                    print_log('equals断言成功')
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
        else:
            print_log("contains断言成功")
        return flag
    except Exception as e:
        error_log("assert_utils模块contains_assert方法报错：%s" % str(traceback.format_exc()))
        raise e



def database_assert(value, actual_result):
    try:
        flag = 0
        for assert_key, assert_value in value.items():
            lists = jsonpath.jsonpath(actual_result, '$..%s' % assert_value)
            try:
                db_res = DataBaseUtil().execute_sql(assert_key)
                int_db_res = db_res[0]
                if lists:
                    if int_db_res == lists[0]:
                        print_log('db_equals断言成功')
                    else:
                        flag = flag + 1
                        print_log("db_equals断言失败：" + str(int_db_res) + "不等于" + "实际结果中"+str(assert_value) + "字段的值")
                else:
                    flag = flag + 1
                    print_log("db_equals断言失败：返回的结果中没有" + str(assert_value) + "")
            except Exception as e:
                error_log("SQL查询语句可能有错，或者查询结果为空，请检查")
                raise e
        return flag

    except Exception as e:
        error_log("assert_utils模块db_equals方法报错：%s" % str(traceback.format_exc()))
        raise e
