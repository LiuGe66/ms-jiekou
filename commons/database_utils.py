# -*- coding: utf-8 -*-            
# Author:liu_ge
# @FileName: database_utils.py
# @Time : 2022/11/11 19:22
from sqlite3 import Cursor

import pymysql


class DataBaseUtil:
    # 创建连接
    def create_conn(self):
        self.conn = pymysql.connect(
            host="shop-xo.hctestedu.com",
            port=3306,
            database="shopxo_hctested",
            user="api_test",
            password="Aa9999!"
        )
        return self.conn

    def execute_sql(self, sql):
        # 创建游标
        self.cs = self.create_conn().cursor()
        # 通过游标执行sql
        self.cs.execute(sql)
        value = self.cs.fetchone()
        self.close_resource()
        return value

    def close_resource(self):
        self.cs.close()
        self.conn.close()


if __name__ == '__main__':
    db = DataBaseUtil()
    re = db.execute_sql("SELECT CAST(original_price AS SIGNED) FROM sxo_cart WHERE id=97;")
    print(re)
    print(type(re))
    a= re[0]
    print(a)

