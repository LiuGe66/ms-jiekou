# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: database_utils.py
# @Time : 2022/11/11 19:22
import MySQLdb

connect = MySQLdb.connect(
    host="47.107.116.139",
    user="root",
    password="admin123",
    database="phpwind",
    port=3306
)
