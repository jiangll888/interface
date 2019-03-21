from util.db_config import OperaDB
from config.config_data import ConfigData
from base.run_method import RunMethod
import json
from jsonpath_rw import jsonpath, parse
from base.handle_header import HandleHeader

class HandleDepend:
    def __init__(self):
        self.op_db = OperaDB()
        self.run_m = RunMethod()
        self.handle_h = HandleHeader()

    def get_data_from_db(self,data):
        config_d1 = ConfigData(data)
        case_id = config_d1.get_depend_case_id()
        sql = "SELECT * FROM `case` where caseid='" + case_id + "';"
        depend_data = self.op_db.get_one(sql)
        return depend_data

    def get_depend_data(self,data):
        depend_data = self.get_data_from_db(data)
        config_d = ConfigData(depend_data)
        self.url = config_d.get_url()
        self.method = config_d.get_method()
        self.header_info = config_d.get_header_info()
        self.run_data = config_d.get_run_data()
        # self.depend_case_id = config_d.get_depend_case_id()
        # self.depend_response_key = config_d.get_depend_reponse_key()
        # self.depend_request_key = config_d.get_depend_request_key()
        self.is_connect = config_d.get_is_connect()
        #self.is_mock = config_d.get_is_mock()

    def run_depend_case(self,data):
        self.get_depend_data(data)
        header = self.handle_h.handle_h(self.header_info)
        # if self.depend_case_id:
        #     self.replace_data(data)
        if header[1]:
            # 发送带cookie
            res = self.run_m.send_request(method=self.method, url=self.url, data=self.run_data, header=header[0],
                                          cookie=header[1])
        else:
            res = self.run_m.send_request(method=self.method, url=self.url, data=self.run_data, header=header[0])
        return res.json()

    def get_data_for_key(self,data):
        res = self.run_depend_case(data)
        config_d2 = ConfigData(data)
        response_key = config_d2.get_depend_reponse_key()
        response_key_list = response_key.split(";")
        key_list = []
        for key in response_key_list:
            json_exe = parse(key)
            madle = json_exe.find(res)
            key_list.append([match.value for match in madle][0])
        is_connect = config_d2.get_is_connect()
        if is_connect:
            return [is_connect.join(key_list)]
        else:
            return key_list

    def replace_data(self,data):
        config_d2 = ConfigData(data)
        request_key = config_d2.get_depend_request_key()
        run_data = config_d2.get_run_data()
        respone_key_list = self.get_data_for_key(data)
        request_key_list = request_key.split(";")
        if not isinstance(run_data,dict):
            run_data = json.loads(run_data)
        for i in range(len(request_key_list)):
            run_data[request_key_list[i]] = respone_key_list[i]
        return json.dumps(run_data)
        # print(run_data)

if __name__ == "__main__":
    h = HandleDepend()
    data = {'caseid': 'qingguo_004', 'casename': 'trans_fee', 'url': 'http://study-perf.qa.netease.com/common/getTransportFee', 'is_run': 1, 'method': 'get', 'param': '{"id":1,"addressDetail":"1"}', 'header_info': '{"cookie":"","header":{"Content-Type": "application/json"}}', 'depend_case_id': 'qingguo_003', 'depend_reponse_key': 'result.list.[0].province;result.list.[0].city;result.list.[0].area', 'depend_request_key': 'addressDetail', 'is_connect': "_", 'expect': '"message":"success"', 'is_connect_db': 0, 'is_mock': 0, 'result': None}
    # r = h.get_data_from_db(data)
    # print(r)
    r = h.replace_data(data)
    print(r)

