import json

class Compare:
    def comp(self,expect,result):
        if not isinstance(expect,str):
            expect = json.dumps(expect)
        if not isinstance(result,str):
            result = json.dumps(result)
        if expect in result:
            return True
        else:
            return False