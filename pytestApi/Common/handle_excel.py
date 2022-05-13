'''
封装读取excel方法
openpyxl .xlsx读写操作
安装 pip install openpyxl
'''
from openpyxl import load_workbook
from Common.handle_path import datas_dir


class HandleExcel():

    def __init__(self,file_path,sheet_name):
        '''
        :param file_path: excel存放路径
        :param sheet_name: 表单名称
        '''
        #加载数据文件
        self.wb = load_workbook(file_path)
        #根据表单名称选择表单
        self.sh = self.wb[sheet_name]

    def read_titles(self):
        '''
        :return: 将excel中第一行的每一列返回为一个列表
        '''
        titles = []
        for item in list(self.sh.rows)[0]:#遍历excel中第一行的每一列
            titles.append(item.value)
        return titles

    def read_data(self):
        '''
        :return:将excel第一行与每一行数据打包成字典以列表返回，作为每一条测试用例
        '''
        all_datas = []
        titles = self.read_titles()
        for item in list(self.sh.rows)[1:]:#遍历excel中数据行的每一列
            values = []
            for val in item:#获取每一行的值
                values.append(val.value)
            res = dict(zip(titles,values)) #title和每一行数据打包成字典
            all_datas.append(res)
        return all_datas

    def close_file(self):
        '''
        :关闭文件
        '''
        self.wb.close()


if __name__ == '__main__':
    he = HandleExcel(file_path=datas_dir + "\data.xlsx", sheet_name="业务流")
    cases = he.read_data()
    print(cases)
    he.close_file()
