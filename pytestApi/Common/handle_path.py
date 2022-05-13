'''
封装路径
'''


import os
#项目基础路径
basedir =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#测试用例路径
cases_dir = os.path.join(basedir,"TestCases")
#测试数据路径
datas_dir = os.path.join(basedir,"TestDatas")
#测试报告
reports_dir = os.path.join(basedir,"Outputs\\reports")
#测试日志
logs_dir = os.path.join(basedir,"Outputs\\logs")
#配置文件
conf_dir = os.path.join(basedir,"Conf")