#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/26 下午9:33
# @Author   : wangbo
import time
import unittest
import os
from BeautifulReport import BeautifulReport

root_path = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(root_path, "cases")
report_path = os.path.join(root_path, "report")
current_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())


def main():
    test_suite = unittest.defaultTestLoader.discover(case_path, pattern='TC_*.py')
    result = BeautifulReport(test_suite)
    report = (current_time + ".html")
    result.report(filename=report,
                  description='广告投放自动化测试',
                  report_dir=report_path,
                  theme='theme_cyan')
    print("用例执行完毕！")


if __name__ == '__main__':
    main()
