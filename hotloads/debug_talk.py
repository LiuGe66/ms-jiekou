# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: debug_talk.py
# @Time : 2022/11/11 0:12
import base64
import hashlib
import os
import random
import time

import yaml
import rsa


class DebugTalk:
    def get_random(self, min_num, max_num):
        return str(random.randint(int(min_num), int(max_num)))

    def read_extract(self, key):
        with open(os.getcwd() + "/" + "/extract.yaml", mode="r", encoding="utf-8") as f:
            result = yaml.load(stream=f, Loader=yaml.FullLoader)
            return result[key]

    def read_config(self, node_key):
        with open(os.getcwd() + "/" + "/config.yaml", mode="r", encoding="utf-8") as f:
            result = yaml.load(stream=f, Loader=yaml.FullLoader)
            return result[node_key]

    def md5(self, args):
        # 指定编码格式字串
        utf8_str = str(args).encode("utf-8")
        # md5加密
        md5_str = hashlib.md5(utf8_str).hexdigest()
        return md5_str

    def bs64(self, args):
        # 指定编码格式字串
        utf8_str = str(args).encode("utf-8")
        bs64_str = base64.b64encode(utf8_str).decode("utf-8")
        return bs64_str

    def creart_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)
        with open("./public.pem", "wb") as f:
            f.write(public_key.save_pkcs1())
        with open("./private.pem", "wb") as f:
            f.write(private_key.save_pkcs1())

    def rsa_encrypt(self, args):
        with open("./hotloads/public.pem", 'rb') as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        # 加密
        byte_str = rsa.encrypt(args.encode("utf-8"), public_key)
        secret_str = base64.b64encode(byte_str).decode("utf-8")
        return secret_str
        # 把字节转化为字符串

    def signs(self, yaml_path):
        all_args_dict = {}
        # 第一步：获取所有参数，包括url,params,data
        with open(os.getcwd() + "/" + yaml_path, encoding="utf-8") as f:
            # 加载yaml文件
            yaml_content = yaml.load(f, Loader=yaml.FullLoader)
            # yaml_content是一个列表,这里对列表循环，得到字典
            for caseinfo in yaml_content:
                # 得到字典测试用例里面所有的key
                caseinfo_keys = caseinfo.keys()
                # 如果request 在测试用例的key里面
                if "request" in caseinfo_keys:
                    # 得到request的值
                    request_value = caseinfo['request']
                    # print(request_value)
                    # 判断url，params,data是否在request的key里面
                    if 'url' in request_value.keys():
                        # print(request_value['url'])
                        url = request_value['url']
                        # 对url进行切割得到参数
                        url_args = url[url.index('?') + 1:]
                        # 对参数进行切割
                        args_list = str(url_args).split('&')
                        # 把列表转化成字典
                        for args in args_list:
                            all_args_dict[args[0:args.index('=')]] = args[args.index('=') + 1:]
                    for key, value in request_value.items():
                        if key in ["params", "data"]:
                            for args_key, args_value in value.items():
                                all_args_dict[args_key] = args_value
                    # 注意事项：如果参数里带有${function()}这种结构，则需要替换
                    # all_args_dict = RequestUtil(DebugTalk()).replace_get_value(all_args_dict)
                    all_args_dict = self.dic_asccii_sort(all_args_dict)

        # 第二步
        new_str = ''
        for key, value in all_args_dict.items():
            new_str = new_str + str(key) + '=' + str(value) + "&"
        # 第三-五步
        appid = 'www'
        appsecret = 'baidu'
        nonce = str(random.randint(10000000, 99999999))
        timestamp = str(time.time())
        new_str = 'appid=' + appid + "&appsecret=" + appsecret + "&" + new_str + '&nonce=' + nonce + '&timestamp=' + timestamp
        # 第六步
        sign = self.md5(new_str).upper()
        return sign

    # 把字典按key的asccii码升序排序
    def dic_asccii_sort(self, args_dict):
        dict_key = dict(args_dict).keys()
        list1 = list(dict_key)
        list1.sort()
        new_dict = {}
        for key in list1:
            new_dict[key] = args_dict[key]
        return new_dict


if __name__ == '__main__':
    DebugTalk().signs("testcases/user_manager/sign.yaml")
