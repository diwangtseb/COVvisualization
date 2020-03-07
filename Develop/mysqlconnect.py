import pymysql
import traceback
import time
import datetime

# mysql connect
def get_conn(host="localhost", user="root", password="bl105610", db='cov'):
    conn = pymysql.connect(host, user, password, db)
    # 创建游标，默认是元组型
    cursor = conn.cursor()  # 执行完成返回结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    conn.close()
    cursor.close()


def insert_history(history):
    """
    插入历史数据
    :return:
    """
    cursor = None
    conn = None

    try:
        print(f"{time.asctime()}开始插入数据")
        conn, cursor = get_conn()
        sqlexit = "select ds from history ORDER BY ds DESC LIMIT 0,1 "
        res = cursor.execute(sqlexit)
        b = cursor.fetchall()
        print(type(b))
        a = time.strftime("%Y-%m-%d", str(b))
        print(a)
        #b1 = str(b)[:10]
        #print(b1)
        # a = str(cursor.fetchall()[0][0])[:10]
        neartime = "2020-01-01"
        '''if res > 0:
            a = cursor.fetchall()[0][0]
            neartime = str(a)[:10]'''
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k, v in history.items():
            if k > neartime:
                # item 格式{"2020-03-03":{"confirm":41, "suspect":0, "heal":0, "dead":1}}
                cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"), v.get("suspect_add"),
                                     v.get("heal"), v.get("heal_add"), v.get("dead"), v.get("dead_add")])
                conn.commit()
        print(f"{time.asctime()}插入历史数据完成")
    except():
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_details(details):
    """
    更新details表
    :return:
    """
    cursor = None
    conn = None
    try:
        conn, cursor = get_conn()
        sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead) " \
              "values(%s,%s,%s,%s,%s,%s,%s)"

        # 对比当前最大时间戳
        sql_query = "select %s=(select update_time from details order by id desc limit 1)"
        cursor.execute(sql_query, details[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新最新数据")
            for item in details:
                print(item)
                cursor.execute(sql, item)
            conn.commit()  # 提交事务 update delete insert 操作
            print(f"{time.asctime()}更新最新数据完毕")
        else:
            print(f"{time.asctime()}已是最新数据！")
    except():
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)
