from Develop.mysqlconnect import insert_history, update_details
from Develop.searchFY import GetDetailsData, GetHistoryData


if __name__ == "__main__":
    urlToday = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    urlHistory = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
    }
    history = GetHistoryData(urlHistory, headers)
    insert_history(history)
    details = GetDetailsData(urlToday, headers)
    update_details(details)
