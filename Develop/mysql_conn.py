import pymysql
import time
import traceback


class MysqlConn(object):

    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host="localhost", user="root", password="bl105610", db='cov')
        # 获取游标
        self.cursor = self.db.cursor()

    # 析构化，析构函数
    def __del__(self):
        self.cursor.close()
        self.db.close()

    def insert_history(self, history):
        """
        插入历史数据
        :return:
        """

        try:
            sqlexit = "select ds from history ORDER BY ds DESC LIMIT 0,1 "
            res = self.cursor.execute(sqlexit)
            validate = (res if(res) else "2020-01-01")
            neartime = (self.cursor.fetchone()[0]).strftime('%Y-%m-%d')
            print(f"{time.asctime()}开始插入数据")

            sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            for k, v in history.items():
                if k > neartime:
                    # item 格式{"2020-03-03":{"confirm":41, "suspect":0, "heal":0, "dead":1}}
                    self.cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"),
                                              v.get("suspect_add"), v.get("heal"), v.get("heal_add"),
                                              v.get("dead"), v.get("dead_add")])
                    self.conn.commit()
            print(f"{time.asctime()}插入历史数据完成")
        except():
            traceback.print_exc()

    def update_details(self, details):
        """
        更新details表
        :return:
        """
        try:
            sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead) " \
                  "values(%s,%s,%s,%s,%s,%s,%s)"

            # 对比当前最大时间戳
            print(details)
            print(details[0][0])
            sql_query = "select %s=(select update_time from details order by id desc limit 1)"
            self.cursor.execute(sql_query, details[0][0])
            if not self.cursor.fetchone()[0]:
                print(f"{time.asctime()}开始更新最新数据")
                for item in details:
                    print(item)
                    self.cursor.execute(sql, item)
                self.conn.commit()  # 提交事务 update delete insert 操作
                print(f"{time.asctime()}更新最新数据完毕")
            else:
                print(f"{time.asctime()}已是最新数据！")
        except():
            traceback.print_exc()
