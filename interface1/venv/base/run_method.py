import requests
import json
import threading

class RunMethod(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        _instance_lock = threading.Lock()

        if not hasattr(cls,"_instance"):
            with _instance_lock:
                if not hasattr(cls,"_instance"):
                    cls._instance = super(RunMethod,cls).__new__(cls)
        return cls._instance

    def send_get(self,url,data=None,header=None,cookie=None):
        if data:
            data = json.loads(data)
        if cookie == None:
            res = requests.get(url=url,params=data,headers=header)
        else:
            res = requests.get(url=url, params=data, headers=header, cookies=cookie)
        return res

    def send_post(self,url,data=None,header=None,cookie=None):
        #data = json.dumps(data)
        if cookie == None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url, data=data, headers=header,cookies=cookie)
        return res

    def send_request(self,method,url,data=None,header=None,cookie=None):
        if method == 'get':
            res = self.send_get(url=url,data=data,header=header,cookie=cookie)
        else:
            res = self.send_post(url=url,data=data,header=header,cookie=cookie)
        return res

if __name__ == '__main__':
    r = RunMethod()
    data = {"phoneArea":"86","phoneNumber":"20000000000","password":"netease123"}
    #data = json.dumps(data)
    header = {
        "Content-Type": "application/json"
    }
    res = r.send_request('post','http://study-perf.qa.netease.com/common/fgadmin/login',data=data,header=header)
    print(res.text)



