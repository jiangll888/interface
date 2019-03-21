from config import settings
from util.db_config import OperaDB
import json
import threading

class ConfigData:
    def __init__(self,data):
        if data:
            self.data = data
        else:
            print("数据不能为空")

    def __new__(cls, *args, **kwargs):
        _instance_lock = threading.Lock()
        if not hasattr(cls,"_instance"):
            with _instance_lock:
                if not hasattr(cls,"_instance"):
                    cls._instance = super(ConfigData,cls).__new__(cls)
        return cls._instance

    def get_case_id(self):
        try:
            return self.data[settings.CASE_ID]
        except:
            return None

    def get_case_name(self):
        try:
            return self.data[settings.CASE_NAME]
        except:
            return None

    def get_url(self):
        try:
            return self.data[settings.URL]
        except:
            return None

    def get_is_run(self):
        try:
            return self.data[settings.IS_RUN]
        except:
            return None

    def get_method(self):
        try:
            return self.data[settings.METHOD]
        except:
            return None

    def get_header_info(self):
        try:
            header = self.data[settings.HEADER_INFO]
            if not isinstance(header,dict):
                header = json.loads(header)
            return header
        except:
            return None

    def get_run_data(self):
        try:
            return self.data[settings.PARAM]
        except:
            return None

    def get_depend_case_id(self):
        try:
            return self.data[settings.DEPEND_CASE_ID]
        except:
            return None

    def get_depend_reponse_key(self):
        try:
            return self.data[settings.DEPEND_RESPONSE_KEY]
        except:
            return None

    def get_depend_request_key(self):
        try:
            return self.data[settings.DEPEND_REQUEST_KEY]
        except:
            return None

    def get_is_connect(self):
        try:
            return self.data[settings.IS_CONNECT]
        except:
            return None

    def get_is_connect_db(self):
        try:
            return self.data[settings.IS_CONNECT_DB]
        except:
            return None

    def get_is_mock(self):
        try:
            return self.data[settings.IS_MOCK]
        except:
            return None

    def get_expect(self):
        try:
            return self.data[settings.EXPECT]
        except:
            return None

    def get_result(self):
        try:
            return self.data[settings.RESULT]
        except:
            return None

    def write_result(self,res,id):
        try:
            op = OperaDB()
            sql = "update `case` set "+settings.RESULT+"=%s where "+ settings.CASE_ID +"=%s;"
            op.insert_data(sql,(res,id))
        except:
            return None

if __name__ == '__main__':
    db = OperaDB()
    #d = db.get_all("SELECT * FROM `case`")
    data = {'caseid': 'qingguo_004', 'casename': 'trans_fee', 'url': 'http://study-perf.qa.netease.com/common/getTransportFee', 'is_run': 1, 'method': 'get', 'param': '{"id":1,"addressDetail":""}', 'header_info': '{"cookie":"","header":{"Content-Type": "application/json"}}', 'depend_case_id': 'qingguo_003', 'depend_reponse_key': 'result:list:[0]:province;result:list:[0]:city;result:list:[0]:area', 'depend_request_key': 'addressDetail', 'is_connect': None, 'expect': '"message":"success"', 'is_connect_db': 0, 'is_mock': 0, 'result': None}

    c = ConfigData(data)
    print(c.get_depend_reponse_key())
    c.write_result('pass','qingguo_001')
    # he = c.get_header_info()
    # print(he)
    # print(he['header'])