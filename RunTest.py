from Util.db_handler import DB
from action.get_rely import get_rely_data
from Util.HttpClient import HttpClient
from action.data_store import rely_data_store


def main():
    db = DB()
    apiList = db.get_api_list()
    print(apiList)
    for api in apiList:
        api_case_list = db.get_api_case(api[0])
        for case in api_case_list:
            rely_list = case[3]
            print(type(rely_list))
            request_data = eval(case[2])
            # 接下俩进行数据依赖处理
            if rely_list:
                request_data = get_rely_data(api[0], case[0], eval(rely_lsit), request_data)
            # 接下来进行接口请求，并获取响应body
            responseObj = HttpClient.request(api[3], api[4], api[5], request_data)
            print(responseObj.status_code)
            # 接下来进行数据依赖存储
            if responseObj.status_code == 200:
                rely_data_store(api[0], case[0], api[1], case[6], request_data, responseObj.json())


if __name__ == "__main__":
    main()
