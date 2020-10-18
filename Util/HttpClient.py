# 此文件主要用于处理接口发送请求并返回响应结果

import requests
import json

class HttpClient(object):
    def __init__(self):
        pass

    @classmethod
    def request(cls,requestUrl,requestMethod,paramsType,requestData = None,headers = None):
        if requestMethod == "post":
            if paramsType == "form":
                # 说明接口请求串从哪方式为表单提交，通过data变量接收
                response = requests.post(url=requestUrl,data=json.dumps(requestData))
                return response
            elif paramsType == "json":
                #说明通过json变量接收传传参

                response =requests.post(url=requestUrl,json=json.dumps(requestData),headers=None)
                return response
        elif requestMethod == "get":
            if paramsType == "url":

                #说明接口的请求参数是直接拼接在url上的
                request_url = "%s%s"%(requestUrl,requestData)
                response = requests.get(url=requestUrl,headers=heads)

            elif paramsType == "params":
                # 说明此接口的ge请求参数是通过params参数接收的
                if isinstance(requestData,dict):


                    response = requests.get(url=requestUrl, params=json.dumps(requestData),headers=heads)
                else:
                    response = requests.get(url=requestUrl, params=requestData, headers=heads)
            return response

if __name__ == "__main__":
    #注册调试
    # requestUrl = "http://39.106.41.11:8080/register/"
    # requestMethod = "post"
    # paramsType = "form"
    # requestData = {"username":"xxxe233sd","password":"dflwe23sd","email":"wcx@qq.com"}
    # response = HttpClient.request(requestUrl,requestMethod,paramsType,requestData)
    # print(response.status_code)
    # print(response.json())

    # 登录调试
    # requestUrl = "http://39.106.41.11:8080/login/"
    # requestMethod = "post"
    # paramsType = "form"
    # requestData = {"username":"xxxe233sd","password":"dflwe23sd","email":"wcx@qq.com"}
    # response = HttpClient.request(requestUrl,requestMethod,paramsType,requestData)
    # print(response.status_code)
    # print(response.json())
    # response = HttpClient.request(requestUrl,requestMethod,paramsType,requestData)

    # 查询博文
    requestUrl = "http://39.106.41.11:8080/getBlogContent/"
    requestMethod = "get"
    paramsType = "url"
    requestData = json.dumps({"articleIds": "2"})
    response = HttpClient.request(requestUrl,requestMethod,paramsType,requestData)
    print(response.status_code)
    print(response.json())
    #response = HttpClient.request(requestUrl,requestMethod,paramsType,requestData)
