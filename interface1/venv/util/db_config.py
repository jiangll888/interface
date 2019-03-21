import pymysql
import threading

class OperaDB(object):
    def __init__(self):
        self.conn = pymysql.connect(
                host = '10.0.4.231',
                #host = 'localhost',
                port = 3306,
                user = 'root',
                passwd='122901',
                db = 'test',
                cursorclass = pymysql.cursors.DictCursor
                #charset = 'utf-8'
            )
        self.cursor = self.conn.cursor()

    def __new__(cls, *args, **kwargs):
        _instance_lock = threading.Lock()
        if not hasattr(cls,"_instance"):
            with _instance_lock:
                if not hasattr(cls,"_instance"):
                    cls._instance = super(OperaDB,cls).__new__(cls)
        return cls._instance

    def get_one(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert_data(self,sql,args=None):
        if args:
            self.cursor.execute(sql,args)
        else:
            self.cursor.execute(sql)
        self.conn.commit()

    def close_database(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    op = OperaDB()
    print(op)
    print(op.get_all("SELECT * FROM `case`;"))
    op.insert_data("update `case` set result=%s where caseid=%s",('pass','qingguo_001'))