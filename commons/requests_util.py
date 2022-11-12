# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: requests_util.py
# @Time : 2022/11/8 13:21
import json
import re
import jsonpath
import requests
from commons.assert_utils import assert_result
from commons.yaml_util import write_yaml, read_yaml
from hotloads.debug_talk import DebugTalk


class RequestUtil:
    sess = requests.session()

    def __init__(self, obj):
        self.obj = obj

    # 统一请求的方法

    def standard_yaml_testcase(self, caseinfo):
        caseinfo_keys = caseinfo.keys()
        # 在Yaml用例里必须有一级关键字name,request,validate
        if "name" in caseinfo_keys and "request" in caseinfo_keys and "validate" in caseinfo_keys:
            request_keys = caseinfo['request'].keys()
            if 'method' in request_keys and "url" in request_keys:
                # 发送请求
                method = caseinfo['request'].pop('method')
                url = caseinfo['request'].pop('url')
                print(caseinfo)
                res = self.send_all_request(method, url, **caseinfo['request'])
                text_result = res.text  # 接收txt响应结果
                status_code = res.status_code
                js_result = ''
                try:
                    js_result = res.json()  # 接收json响应结果
                except():
                    print('响应不是json数据格式')

                print(res.text)
                # 提取需要关联的值，并写入extract.yaml
                if 'extract' in caseinfo.keys():
                    for key, value in caseinfo['extract'].items():
                        if '(.*?)' in value or "(.*+)" in value:  # 正则提取
                            reg_value = re.search(value, text_result)
                            if reg_value:
                                data = {key: reg_value.group(1)}
                                write_yaml("extract.yaml", data)
                            else:
                                print('正则表达式可能有误，或者接口请求失败，未提取到中间变量')
                        else:
                            js_value = jsonpath.jsonpath(js_result, value)
                            if js_value:
                                data = {key: js_value[0]}
                                write_yaml("extract.yaml", data)
                            else:
                                print('jsonpath表达式可能有误，或者接口请求失败，未提取到中间变量')
                # 断言：
                expect_result = caseinfo["validate"]
                actual_result = js_result
                all_flag = assert_result(expect_result, actual_result, status_code)
                if all_flag == 0:
                    print("{}业务断言成功".format(caseinfo["name"]))
                else:
                    assert 1 == 2, print("{}业务断言失败".format(caseinfo["name"]))

            else:
                print("request下面必须包含method,url这两个关键字。")
        else:
            print("在Yaml用例里必须有一级关键字name,request,validate。")

    def send_all_request(self, method, url, **kwargs):
        # method统一小写
        method = str(method).lower()
        # url通过${key}取值
        url = self.replace_get_value(url)
        # headers,params,data,json通过${key}取值
        for key, value in kwargs.items():
            if key in ["headers", "params", "data", "json"]:
                kwargs[key] = self.replace_get_value(value)
            elif key == "files":
                for file_key, file_value in value.items():
                    value[file_key] = open(file_value, "rb")
                    print(value)
        # 发送请求：
        res = RequestUtil.sess.request(method, url, **kwargs)
        print("request_utils88行==================================================",res.text)
        return res

    # 封装替换取值的方法
    # 注意1：可能是(url,params,data,json,headers)取值
    # 注意2：数据类型可能是：int,float,string,list,dict
    def replace_get_value(self, data):
        if data:
            # 保存传入的数据类型：
            data_type = type(data)
            # 把不同类型的数据转化为字串，因为字串才能替换：
            if isinstance(data, list) or isinstance(data, dict):
                str_data = json.dumps(data)
            else:
                str_data = str(data)
            # 替换：
            for i in range(1, str_data.count("${") + 1):
                if "${" in str_data and "}" in str_data:
                    start_index = str_data.index("${")
                    end_index = str_data.index("}", start_index)
                    old_value = str_data[start_index:end_index + 1]
                    print(old_value)
                    # 反射：通过类的对象和方法名字符串调用方法
                    # 得到方法名
                    function_name = old_value[2:old_value.index("(")]
                    print(function_name)
                    # 得到参数
                    args_value = old_value[old_value.index("(") + 1:old_value.index(")")]
                    print("args_value:{}".format(args_value))
                    if args_value != "":
                        # 有参数，分割参数
                        all_args_value = args_value.split(",")
                        new_value = getattr(DebugTalk(), function_name)(*all_args_value)
                        print(new_value)
                    else:
                        # 没有参数
                        new_value = getattr(DebugTalk(), function_name)()
                        print(new_value)
                    # 把旧的表达式替换成新的值
                    str_data = str_data.replace(old_value, str(new_value))
            # 还原数据类型
            if isinstance(data, list) or isinstance(data, dict):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
            return data  # 返回值
        else:
            print('有数据未填充，或者反例设计数据为空')
            return data  # 返回值
