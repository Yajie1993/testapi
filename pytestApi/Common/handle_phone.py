# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 14:03
# @Author  : Yajie.Li
# @FileName: phone_number.py
# @Software: PyCharm
# @Address: ZG, Wuhan, China


prefix = [
135,136,137,138,139,147,150,151,152,157,158,159,178,182,183,184,187,188,198,
 130,131,132,145,155,156,175,176,185,186,166,
133,153,173,177,180,181,189,199
]
import random
from Common.handle_db import HandleDB
from Common.handle_config import conf
from Common.handle_requests import send_requests

def get_old_phone():
    user = conf.get("data","user")
    passwd = conf.get("data", "passwd")
    send_requests("post","member/register",{"mobile_phone":user,"pwd":passwd})
    return user,passwd

def generator_new_phone():
    db= HandleDB()
    while True:
        phone = __generator_phone()
        if db.get_count("SELECT * from futureloan.member where mobile_phone = '{}'".format(phone)) ==0:
            db.close()
            return phone

def __generator_phone():
    index = random.randint(0,len(prefix)-1)
    phone = str(prefix[index]) #前三位
    for i in range(0,8):#生成后八位
        phone += str(random.randint(0,9))
    return phone

# def check_phone_in_db():
# a=generator_new_phone()
# print(a)