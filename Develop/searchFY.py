import requests
import json
import time


def GetDetailsData(url, headers):
    """
        爬取数据
        :param url:
        :param headers:
        :return:
        """
    r = requests.get(url, headers)
    res = json.loads(r.text)
    data_all = json.loads(res['data'])
    details = []  # 当日详细数据

    update_time = data_all["lastUpdateTime"]
    data_country = data_all["areaTree"]  # list 25个国家
    data_province = data_country[0]["children"]  # 中国各省
    for pro_infos in data_province:
        province = pro_infos["name"]
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return details


def GetHistoryData(url, headers):
    """
    爬取数据
    :param url:
    :param headers:
    :return:
    """
    r = requests.get(url, headers)
    res = json.loads(r.text)
    data_all = json.loads(res['data'])
    history = {}  # 历史数据
    for i in data_all["chinaDayList"]:
        ds = "2020."+i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式，由于数据库是datetime类型
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead,
                       "confirm_add": 0, "suspect_add": 0, "heal_add": 0, "dead_add": 0}
    for i in data_all["chinaDayAddList"]:
        ds = "2020." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式，由于数据库是datetime类型
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})
    return history
