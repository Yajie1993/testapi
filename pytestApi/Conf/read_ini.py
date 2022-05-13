from configparser import ConfigParser
import os


#1.实例化
conf = ConfigParser()

# 2.读取配置文件
conf.read("testapi.ini",encoding="utf-8")

# 3.读取某一项配置的值 get 全部是字符串
value = conf.get("logs","name")
print(value)


# # 4.写入 set
# conf.set("logs","name","py")
# # 5.写入文件 write
# print(os.getcwd())
# conf.write(open(os.getcwd()+"\testapi.ini","w",encoding="utf-8"))