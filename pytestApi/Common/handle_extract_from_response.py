# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 16:30
# @Author  : Yajie.Li
# @FileName: handle_extract_from_response.py
# @Software: PyCharm
# @Address: ZG, Wuhan, China
from jsonpath import jsonpath
from Common.handle_data import EnvData


def extract_from_response(extract_exprs,response):
    '''

    :param extract_exprs: jsonpath表达式
    :param response: http请求后响应结果
    :return:
    '''
    #将提取表达式转换成字典
    extract_dict = eval(extract_exprs)
    # 遍历字典，key作为全局变量名，value是jsonpath表达式
    for key,value in extract_dict.items():
        res = str(jsonpath(response,value)[0])
        setattr(EnvData,key,res)


if __name__ == '__main__':
    s = '{"member_id":"$..id","token":"$..token"}'
    resp = {'id': 34326684, 'leave_amount': 0.0, 'mobile_phone': '15928016994', 'reg_name': '起1个名字', 'reg_time': '2022-04-18 17:29:47.0', 'type': 1, 'token_info': {'token_type': 'Bearer', 'expires_in': '2022-04-18 17:34:47', 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjM0MzI2Njg0LCJleHAiOjE2NTAyNzQ0ODd9.NuFJjzATzLDfLYmtIALnH18gT5g7Nyj4xNouxmSwYRirn3XRyaBQg9fhHt6udTgfK0gyp9_0aD4exDOJz6PF8w'}}
    extract_from_response(s,resp)
    print(EnvData.__dict__)