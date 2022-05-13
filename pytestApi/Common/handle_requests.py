'''
封装http请求
'''
import requests
from Common.handle_logger import logger
from Common.handle_config import conf

def __handle_header(token=None):
    headers = {"X-Lemonban-Media-Type": "lemonban.v2",}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers

def __pre_url(url):
    base_url = conf.get("sever", "base_url")
    if url.startswith("/"):
        url = base_url + url
    else:
        url = base_url + "/" + url
    return url

def __pre_data(data):
    '''
    :param data:
    :return: 如果data是字符串，转换成字典对象
    '''
    if data is not None and isinstance(data,str):
        #如果有null，替换成None
        if data.find("Null") != -1:
            data.replace("Null","None")
        else:
            #使用eval将字符串替换成字典，如果表达式涉及计算，会自动计算
            data = eval(data)
    return data


def send_requests(method,url,datas=None,token=None,**kwargs):
    method = str(method).lower()
    headers = __handle_header(token)
    url = __pre_url(url)
    datas = __pre_data(datas)
    res = None
    # sess = requests.Session()
    logger.info("请求头为：{}".format(headers))
    logger.info("请求方式为：{}".format(method))
    logger.info("请求url为：{}".format(url))
    logger.info("请求数据为：{}".format(datas))
    if method == 'get':
        res = requests.request(method=method, url=url, params=datas, headers=headers,**kwargs)
    elif method == 'post':
        res = requests.request(method=method, url=url, json=datas,headers=headers, **kwargs)
    else:
        pass
    logger.info("响应状态码为：{}".format(res.status_code))
    logger.info("响应数据为：{}".format(res.json()))
    return res