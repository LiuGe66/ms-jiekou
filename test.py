# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: test.py
# @Time : 2022/11/15 22:53
import jsonpath

dict1 = {
    "name": "liuge",
    "age": 10000,
    "site": "home"
}

res = jsonpath.jsonpath(dict1, "$.namyyye")
print(res)
print(type(res))