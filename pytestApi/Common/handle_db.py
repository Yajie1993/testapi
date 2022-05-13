'''
封装数据库
'''
import pymysql
from Common.handle_config import conf

class HandleDB():

    def __init__(self):
        # 连接数据库，创建游标
        # 1.建立连接
        self.conn = pymysql.connect(
            host=conf.get("mysql", "host"),
            port=conf.getint("mysql", "port"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "password"),
            database=conf.get("mysql", "database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor  # 结果返回为字典
        )
        # 2.创建游标
        self.cur = self.conn.cursor()

    def select_one_data(self,sql):
        #获取一条数据
        self.conn.commit() #提交同步最新数据
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_all_data(self,sql):
        #获取所有数据
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self,sql):
        #获取条数
        self.conn.commit()
        return self.cur.execute(sql)

    def update(self,sql):
        #对数据库进行增删改的操作
        self.conn.commit()
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        #关闭
        self.cur.close()
        self.conn.close()
