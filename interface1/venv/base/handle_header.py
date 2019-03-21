from config import settings
import requests,json

class HandleHeader:
    def __init__(self,filename=None):
        if filename == None:
            self.filename = settings.COOKIE_FILE
        else:
            self.filename = filename

    def read_cookie(self):
        try:
            with open(self.filename,"r") as fp:
                json_data = json.load(fp)
            return json_data
        except:
            print("读取cookie出错")

    def write_cookie(self,res):
        cookie = res.cookies
        cookie = requests.utils.dict_from_cookiejar(cookie)
        with open(self.filename,"w") as fp:
            #fp.truncate()
            json.dump(cookie,fp)

    def handle_h(self, header_info):
        headers = []
        if settings.HEADER in header_info:
            headers.append(header_info[settings.HEADER])
        else:
            headers.append(None)
        if settings.COOKIE in header_info:
            headers.append(self.read_cookie())
        else:
            headers.append(None)
        if settings.IS_WRITE in header_info:
            headers.append(header_info[settings.IS_WRITE])
        else:
            headers.append(None)
        return headers

if __name__ == "__main__":
    h = HandleHeader()
    r = h.read_cookie()
    print(type(r))