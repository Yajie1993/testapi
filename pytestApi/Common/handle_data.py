import re
from Common.handle_config import conf
import json

class EnvData:
    '''
    存储用例中需要用到的数据
    '''
    pass

def clear_EnvData_attrs():
    '''
    删除EnvData类中的变量
    '''
    values = dict(EnvData.__dict__.items())
    for key,value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData,key)



#一条用例涉及数据替换
def replace_mark_with_data(case,mark,new_data):
    '''
    :param case: excel当中读取的一条数据，是个字典
    :param mark:数据当中的占位符 #值#
    :param new_data:要替换mark的真实数据
    '''
    for key,value in case.items():
        if case[key] is not None and isinstance(case[key],str):
            if case[key].find(mark) != -1:
                case[key] = case[key].replace(mark,new_data)
    return case

def replace_case_by_regular(case):
    '''
    :param case: 从excel读取出来的一条用例数据
    :return:全部替换后的用例数据
    '''
    #把case字典(从excel读取出来的一条用例数据)转换成字符串
    case_str = json.dumps(case)
    #替换
    new_case = replace_by_regular(case_str)
    #把替换后的字符串转为字典
    case_dic = json.loads(new_case)
    return case_dic

def replace_by_regular(data):
    '''
    将字符串当中，匹配#(.+?)#部分，替换对应的真实数据
    :param data: 字符串
    :return:
    '''
    res = re.findall("#(.+?)#",data) #如果没有找到，返回的是空列表
    if res:
        for item in res:
            try:
                value = conf.get("data",item)
            except:
                try:
                    value = getattr(EnvData,item)
                except AttributeError:
                    continue
            data = data.replace("#{}#".format(item),value)
    return data
