#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021/3/26 下午10:06
# @Author   : wangbo
# coding:utf8
"""
小程序自动化测试报告邮件
"""
import smtplib
import os
import zipfile
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

# from config import out_path, cur_path
# from common.configJson import get_json
# from common.reportData import get_case_info
from config import out_path, current_path, report_path


class MyEmail:
    def __init__(self):
        self.user = ''
        self.pwd = ''
        # self.to_list = ['wangbo4@mafengwo.com']
        self.to_list = []
        self.cc_list = []
        self.tag = '媒资仓接口自动化构建结果'
        self.annex = None
        self.mail_html = None
        self.result = None
        self.color = None
        self.pre_content = None
        self.after_content = None
        # self.type = get_json()['version_type']
        # self.code = get_json()['version_code']
        # self.device = get_json()['device']
        # self.start_time = get_json()['start_time']

    def send(self, result=0):
        """
        发送邮件
        """

        try:
            server = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465)
            server.login(self.user, self.pwd)
            server.sendmail("<%s>" % self.user, self.to_list, self.get_attach(result))
            server.close()
            print("send email successful")
        except smtplib.SMTPException as e:
            print("send email failed %s" % e)

    def get_attach(self, result):
        """
        构造邮件内容
        """
        self.compressed_file()
        part = MIMEMultipart()
        if self.tag:
            part["Subject"] = self.tag
        if self.user:
            part["From"] = '任永成superman<%s>' % self.user
        if self.to_list:
            part["To"] = ";".join(self.to_list)
        if self.cc_list:
            part["Cc"] = ";".join(self.cc_list)
        # all_case, suc_case, fail_case, err_case = get_case_info(result)
        # if fail_case == '0':
        #     self.color = 'green'
        #     self.result = '通过'
        # else:
        #     self.color = 'red'
        #     self.result = '{}条用例未通过'.format(fail_case)
        self.mail_html = '''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>自动化构建结果</title>
            </head>
            <body>
            <p>Dear&nbsp;All:</p>
            <p>本次自动化已构建完成</p>
            <p>详情查阅附件，如有问题请联系<a href="mailto:rychh@163.com">任永成</a></p>

            </body>
            </html>'''

        part.attach(MIMEText(self.mail_html, 'html', 'utf-8'))
        if self.annex:
            with open(self.annex, 'rb') as f:
                # 这里附件的MIME和文件名，这里是xls类型
                mime = MIMEBase('zip', 'zip', filename='output.zip')
                # 加上必要的头信息
                mime.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', 'output.zip'))
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                # 把附件的内容读进来
                mime.set_payload(f.read())
                # 用Base64编码
                encoders.encode_base64(mime)
                part.attach(mime)
        return part.as_string()

    def compressed_file(self, dir_path=report_path):
        file_news = dir_path + '.zip'  # 压缩后文件夹的名字
        with zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED) as z:  # 参数一：文件夹名
            for d_path, d_names, filenames in os.walk(dir_path):
                f_path = d_path.replace(dir_path, '')  # 这一句很重要，不replace的话，就从根目录开始复制
                f_path = f_path and f_path + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
                for filename in filenames:
                    z.write(os.path.join(d_path, filename), f_path + filename)
                    print('压缩成功:', filename)
        self.annex = os.path.join(current_path, 'output.zip')


if __name__ == "__main__":
    # my = MyEmail()
    # my.send()
    MyEmail().compressed_file()
