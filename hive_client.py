#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/9/7
# pip install pyhive
# pip install thrift
# pip install thrift-sasl
# yum install cyrus-sasl-plain cyrus-sasl-devel cyrus-sasl-gssapi  cyrus-sasl-md5
# pip install sasl
import time
import requests
import json
from pyhive import hive
import pandas as pd



def hive_query(sql):
    conn = hive.Connection(host='192.168.160.25', port='10000', auth='CUSTOM', username='hive', password='hive')
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def time_create():
    pday = int(time.strftime('%Y%m%d', time.localtime()))
    phour = time.localtime().tm_hour
    return pday, phour


def put_alert(url, message):
    # {"url":"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx", "message":"test"}
    ptime = time.strftime('%Y-%m-%d %H:%M:%S')
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    # message = message[0:10000]
    botmessage = "------------------------------" + '\n' \
                 + "           ff_report" + '\n' \
                 + "------------------------------" + '\n' \
                 +  message + '\n' \
                 + "时间: " + ptime + '\n' \
                 + "------------------------------"
    # print(botmessage)
    try:
        body = {
            "msg_type": "text",
            "content": {
                "text": botmessage
            }
        }
        # print(body)
        requests.post(url, json.dumps(body), headers=headers)
    except Exception as e:
        print(e)


def put_file(message, filename):
    # {"url":"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx", "message":"test"}
    botmessage = "------------------------------" + '\n' \
                 + "           ff_report" + '\n' \
                 + "------------------------------" + '\n' \
                 +  message + '\n' \
                 + "时间: " + ptime + '\n' \
                 + "------------------------------"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(botmessage)



