# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: requests_util.py
# @Time : 2022/11/8 13:21
import requests


class RequestUtil:
    sess = requests.session()

    # 统一请求的方法
    def send_all_request(self, method, url, **kwargs):
        res = RequestUtil.sess.request(method, url, **kwargs)
        return res
