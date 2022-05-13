
import json
import pytest
from Common.handle_requests  import send_requests
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.handle_logger import logger
from Common.handle_data import replace_mark_with_data,EnvData

ex = HandleExcel(file_path=datas_dir+"\data.xlsx",sheet_name="充值")
cases = ex.read_data()
ex.close_file()

@pytest.mark.usefixtures("ses")
@pytest.mark.usefixtures("clear_EnvData")
class TestRecharge:

    @pytest.mark.parametrize("case",cases)
    def test_recharge(self,case,db):

        logger.info("开始执行{}，{}".format(case["id"],case["title"]))

        if case["request_data"].find("#member_id#") != -1:
            case = replace_mark_with_data(case,"#member_id#",str(EnvData.member_id))

        if case["check_sql"]:
            leave_amount_before = db.select_one_data(case["check_sql"])["leave_amount"]
            recharge_money = json.loads(case["request_data"])["amount"]
            except_leave_amount = round(float(leave_amount_before) + recharge_money,2)
            case = replace_mark_with_data(case, "#money#", str(except_leave_amount))

        resp = send_requests(case["method"], case["url"], (case["request_data"]),token=EnvData.token)
        logger.info("期望结果： {}".format(case["except"]))

        try :
            assert resp.json()["code"]==json.loads(case["except"])["code"]
            assert resp.json()["msg"]==json.loads(case["except"])["msg"]
            if case["check_sql"]:
                assert resp.json()["data"]["id"]== json.loads(case["except"])["data"]["id"]
                assert resp.json()["data"]["leave_amount"]== json.loads(case["except"])["data"]["leave_amount"]
                leave_amount_after = float(db.select_one_data(case["check_sql"])["leave_amount"])
                assert leave_amount_after==json.loads(case["except"])["data"]["leave_amount"]
        except:
            logger.exception("断言失败，用例不通过")
            raise

        else:
            logger.info("用例成功")
        logger.info("##########  此用例测试结束  #############")

