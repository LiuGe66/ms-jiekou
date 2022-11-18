# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: logger_utils.py
# @Time : 2022/11/12 18:37
import logging
import os
import time
import yaml
import colorlog


# 函数,用于日志输出
# 错误日志
def error_log(message):
    LoggerUtils().create_log().error(message)
    raise AssertionError(message)


def print_log(message):
    LoggerUtils().create_log().info(message)
    # raise Exception(message)


class LoggerUtils:

    def get_new_path(self):
        return os.getcwd().split("commons")[0]

    def read_config_log(self, one_key, two_key):
        with open(self.get_new_path() + "/config.yaml", mode="r", encoding="utf-8") as f:
            result = yaml.load(stream=f, Loader=yaml.FullLoader)
            return result[one_key][two_key]

    def create_log(self):
        # 1.创建日志对象
        self.logger = logging.getLogger(name="log")
        # 设置全局日志级别(从低到高:debug<info<warning<error<critical)
        self.logger.setLevel(logging.DEBUG)
        # 文件日志
        if not self.logger.handlers:
            #################################信息日志#################################
            # 文件日志的名称规范

            format_string2 = "%Y-%m-%d %H-%M-%S"
            log_file_path = self.get_new_path() + "/logs/" + self.read_config_log("log", "log_file_name") + str(time.strftime('%Y_%m_%d   %H_%M_%S',time.localtime(time.time()))) + ".log"
            # 2.创建一个文件日志控制控制器
            file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
            # 3.设置文件日志级别
            file_log_level = self.read_config_log("log", "log_level")
            if file_log_level == "debug":
                file_handler.setLevel(logging.DEBUG)
            elif file_log_level == "info":
                file_handler.setLevel(logging.INFO)
            elif file_log_level == "warning":
                file_handler.setLevel(logging.WARNING)
            elif file_log_level == "error":
                file_handler.setLevel(logging.ERROR)
            elif file_log_level == "critical":
                file_handler.setLevel(logging.CRITICAL)
            else:
                file_handler.setLevel(logging.DEBUG)
            # 4.设置文件日志的格式
            file_handler.setFormatter(logging.Formatter(self.read_config_log("log", "log_format")))
            # 5.将文件日志控制器加入日志对象
            self.logger.addHandler(file_handler)

            #################################控制台日志#################################
            # 1.创建一个控制台日志控制控制器
            console_handler = logging.StreamHandler()
            # 2.设置控制台日志级别
            console_log_level = self.read_config_log("log", "log_level")
            if console_log_level == "debug":
                console_handler.setLevel(logging.DEBUG)
            elif console_log_level == "info":
                console_handler.setLevel(logging.INFO)
            elif console_log_level == "warning":
                console_handler.setLevel(logging.WARNING)
            elif console_log_level == "error":
                console_handler.setLevel(logging.ERROR)
            elif console_log_level == "critical":
                console_handler.setLevel(logging.CRITICAL)
            else:
                console_handler.setLevel(logging.DEBUG)
            # 3.设置文件日志的格式
            console_handler.setFormatter(logging.Formatter(self.read_config_log("log", "log_format")))
            # 4.将文件日志控制器加入日志对象
            self.logger.addHandler(console_handler)

        return self.logger