import unittest
import ddt
from util.db_config import OperaDB
from base.run_main import RunMain
import HTMLTestRunner

# op = OperaDB()
# data = op.get_all("SELECT * FROM `case`")
data = {'caseid': 'qingguo_001', 'casename': 'login', 'url': 'http://localhost:9000/get/return/cookies', 'is_run': 1,
        'method': 'get', 'header_info': '{"is_write":1}', 'depend_case_id': None, 'depend_reponse_key': None,
        'depend_request_key': None, 'is_connect': None, 'expect': '返回cookies信息成功', 'is_connect_db': 0, 'is_mock': 0,
        'result': ''}

@ddt.ddt
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = RunMain()

    @ddt.data(data)

    @ddt.unpack
    def test01(self,*args,**kwargs):
        #print(kwargs)
        res = self.r.run_main(kwargs)
        #print(res)

    # @classmethod
    # def tearDownClass(cls):
    #     op.close_database()

if __name__ == '__main__':
    #unittest.main()
    # test_suite = unittest.TestSuite()  # 创建一个测试集合
    # test_suite.addTest(Test('test02'))  # 测试套件中添加测试用例
    # suite = unittest.TestSuite()
    # suite.addTest(Test('test01'))
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    with open("../report/test.html","wb") as fp:
        HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="interface_test_report",description="test").run(suite)
