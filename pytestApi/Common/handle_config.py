from configparser import ConfigParser
from Common.handle_path import conf_dir


class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path,encoding="utf-8")

file_path = conf_dir+"\\testapi.ini"
conf = HandleConfig(file_path)