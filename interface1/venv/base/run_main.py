import os,sys
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.join(os.path.dirname(os.getcwd()),"Lib\\site-packages"))
from config.config_data import ConfigData
from base.run_method import RunMethod
from base.handle_header import HandleHeader
from config.handle_depend import HandleDepend
from util.compare import Compare
from base.handle_list_dict import handle

class RunMain:
    def __init__(self):
        self.run_m = RunMethod()
        self.handle_h = HandleHeader()

    def handle_data(self):
        config_d = ConfigData(self.data)
        self.case_id = config_d.get_case_id()
        self.case_name = config_d.get_case_name()
        self.url = config_d.get_url()
        self.method = config_d.get_method()
        self.header_info = config_d.get_header_info()
        self.run_data = config_d.get_run_data()
        self.is_run = config_d.get_is_run()
        self.depend_case_id = config_d.get_depend_case_id()
        self.depend_response_key = config_d.get_depend_reponse_key()
        self.depend_request_key = config_d.get_depend_request_key()
        self.is_connect = config_d.get_is_connect()
        self.is_connect_db = config_d.get_is_connect_db()
        self.is_mock = config_d.get_is_mock()
        self.expect = config_d.get_expect()


    def run_main(self,data):
        self.data = data
        self.handle_data()
        header = self.handle_h.handle_h(self.header_info)
        if self.is_run:
            if self.depend_case_id:
                h = HandleDepend()
                self.run_data = h.replace_data(data)
            if self.run_data:
                self.run_data = handle(self.run_data)
            if header[1]:
                #发送带cookie
                res = self.run_m.send_request(method=self.method,url=self.url,data=self.run_data,header=header[0],cookie=header[1])
            else:
                res = self.run_m.send_request(method=self.method,url=self.url,data=self.run_data,header=header[0])
            #写入cookie
            if header[2]:
                self.handle_h.write_cookie(res)
            compare = Compare()
            config_d1 = ConfigData(self.data)
            print(self.expect,res.text)
            if compare.comp(self.expect,res.text):
                print("pass")
                config_d1.write_result("pass",self.case_id)
            else:
                print("fail")
                config_d1.write_result("fail", self.case_id)

if __name__ == "__main__":
    data = {'caseid': 'qingguo_001', 'casename': 'login', 'url': 'http://localhost:9000/get/return/cookies', 'is_run': 1, 'method': 'get', 'header_info': '{"is_write":1}', 'depend_case_id': None, 'depend_reponse_key': None, 'depend_request_key': None, 'is_connect': None, 'expect': '返回cookies信息成功', 'is_connect_db': 0, 'is_mock': 0, 'result': ''}
    #print(list(data.keys()))
    r = RunMain()
    r.run_main(data)


