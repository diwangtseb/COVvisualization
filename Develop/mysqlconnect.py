import pymysql
import traceback
import time


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
        dic = history
        print(f"{time.asctime()}开始插入数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k, v in dic.items():
            # item 格式{"2020-03-03":{"confirm":41, "suspect":0, "heal":0, "dead":1}}
            cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("suspect"), v.get("suspect_add"),
                                 v.get("heal"), v.get("heal_add"), v.get("dead"), v.get("dead_add")])
            conn.commit()
        print(f"{time.asctime()}插入历史数据完成")
    except():
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_details(detail):
    """
    更新details表
    :return:
    """
    cursor = None
    conn = None
    try:
        li = detail  # 0是历史数据字典，1是最新详细数据列表
        conn, cursor = get_conn()
        sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead) " \
              "values(%s,%s,%s,%s,%s,%s,%s)"

        # 对比当前最大时间戳
        sql_query = "select %s=(select update_time from details order by id desc limit 1)"
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
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
