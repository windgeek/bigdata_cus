#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/9/7
# pip install presto-python-client
import prestodb
import time
import requests
import json
from retry import retry


@retry()
def presto_query(sql):
    conn = prestodb.dbapi.connect(
        host='192.168.160.25',  # host位置
        port=9086,  # 端口位置
        user='default',  # 用户名
        catalog='hive',  # 使用的hive
        schema='default',  # 使用的schema，默认是default，可以不改
        http_scheme='http'  # 后面的暂时不添加，http的添加后报错,
        # auth=prestodb.auth.BasicAuthentication("", “”)
    )
    # conn._http_session.verify = ‘./ presto.pem’  # 校验文件存储位置，这个应该是默认位置
    cur = conn.cursor()
    cur.execute(sql)  # sql语句
    rows = cur.fetchall()
    print(rows)
    return rows


def time_create():
    pday = int(time.strftime('%Y%m%d', time.localtime()))
    phour = time.localtime().tm_hour
    return pday, phour


def put_alert(url, message):
    # {"url":"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx", "message":"test"}
    ptime = time.strftime('%Y-%m-%d %H:%M:%S')
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    botmessage = "------------------------------" + '\n' \
                 + "           dsp_pi_logreport" + '\n' \
                 + "------------------------------" + '\n' \
                 + "报警: " + message + '\n' \
                 + "报警时间: " + ptime + '\n' \
                 + "------------------------------"
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


