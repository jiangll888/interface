from util.send_mail import SendMail
from util.db_config import OperaDB

class RunMail:
    def send_mail(self,filename=None):
        op = OperaDB()
        se = SendMail()

        result_list = op.get_all("select result from `case`;")
        result_list1 = [[value for key,value in d.items()][0] for d in result_list]
        pass_count = 0.0
        fail_count = 0.0
        for i in result_list1:
            if i == "pass":
                pass_count += 1
            else:
                fail_count += 1
        print(pass_count,fail_count)
        count_num = pass_count +fail_count
        result = "%.2f%%" % (pass_count/count_num*100)
        print(result)
        content = "本次自动化测试结果：通过"+ str(pass_count) + "个，失败" + str(fail_count) +"个，通过率为" \
           + str(result)
        se.send_mail(["jiangliulin@163.com"],"自动化结果",content,filename)

if __name__ == "__main__":
    r = RunMail()
    r.send_mail("../report/test.html")