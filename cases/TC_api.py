#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/26 下午9:05
# @Author   : wangbo
import unittest
from ddt import ddt, unpack, data

from Util.HttpClient import HttpClient
from Util.db_handler import DB
from action.get_rely import get_rely_data

db = DB()


def get_api_list():
    return db.get_api_list()


def get_api_case():
    new_case = []
    api_list = get_api_list()
    for api in api_list:
        api_case_list = db.get_api_case(api[0])
        for case in api_case_list:
            rely_list = case[3]
            request_data = eval(case[2])
            # 接下俩进行数据依赖处理
            if rely_list:
                request_data = get_rely_data(api[0], case[0], eval(rely_list), request_data)
            api.append(request_data)
            new_case.append(api)
    return new_case


@ddt
class ApiTest(unittest.TestCase):

    def setUpClass(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def tearDownClass(self) -> None:
        pass

    @data(*get_api_case())
    @unpack
    def test_case(self, api_id, api_name, file_name, r_url, r_method, p_type, rely_db, status, ctime, request_data):
        """{api_name}"""
        responseObj = HttpClient.request(r_url, r_method, p_type, request_data)
        # 接下来进行数据依赖存储
        self.assertEqual(responseObj, 200)
