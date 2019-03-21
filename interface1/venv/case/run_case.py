import unittest
import os,time
import HTMLTestRunner
from case.mail import RunMail


class RunCase:
    report_file = ""
    def run_testcase(self):
        base_dir = os.path.abspath(os.getcwd())
        discover = unittest.defaultTestLoader.discover(
            start_dir=base_dir,
            pattern="test*.py",
            top_level_dir=None
        )
        filename = time.strftime("%Y-%m-%d %H_%M_%S") + ".html"
        RunCase.report_file = os.path.join(os.getcwd(),"../report/"+filename)
        with open(RunCase.report_file,"wb") as fp:
            HTMLTestRunner.HTMLTestRunner(fp).run(discover)

    def send_main(self):
        mail = RunMail()
        mail.send_mail(RunCase.report_file)

if __name__ == "__main__":
    r = RunCase()
    r.run_testcase()
    #r.send_main()