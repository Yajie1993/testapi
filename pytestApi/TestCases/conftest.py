import pytest
from jsonpath import jsonpath

from Common.handle_data import clear_EnvData_attrs,EnvData
from Common.handle_db import HandleDB
from Common.handle_phone import get_old_phone
from Common.handle_requests import send_requests

@pytest.fixture(scope="class")
def clear_EnvData():
    clear_EnvData_attrs()

@pytest.fixture(scope="session",autouse=True)
def db():
    db = HandleDB()
    yield db
    db.close()

@pytest.fixture(scope="class")
def ses():
    #调用登陆接口，获取id 和 token，设置为类属性
    user,passwd = get_old_phone()
    resp = send_requests("post","member/login",{"mobile_phone":user,"pwd":passwd})
    resp = resp.json()
    setattr(EnvData,"member_id",jsonpath(resp,"$..id")[0])
    setattr(EnvData, "token", jsonpath(resp, "$..token")[0])