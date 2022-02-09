!/usr/bin/env python
#-*- coding: utf-8 -*-

import commands
import requests
import json
import pandas as pd
from Mail_html import send_mail
from texttable import Texttable

ResourceManagerMap = {}
ResourceManagerMap['rm1'] = "192.168.160.17"
ResourceManagerMap['rm2'] = "192.168.160.18"
ResourceManagerUrl = "192.168.160.17"
queue_per = 95
try:
    for name, url in ResourceManagerMap.items():
        result = commands.getstatusoutput('yarn rmadmin -getServiceState %s' % name)
        if result[1] == "active": ResourceManagerUrl = url
except Exception:
    pass

APPLICATION_MASTER = "http://%s:8088/ws/v1/cluster/apps?state=RUNNING" % ResourceManagerUrl
r = requests.get(APPLICATION_MASTER)
html = r.text
str_html = html.encode("utf-8")
json_dic = json.loads(str_html)
app = json_dic['apps']['app']
df = pd.DataFrame(app)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df_que_per = df[['queueUsagePercentage']]
df_new = df[['id','queue','queueUsagePercentage']]
df_que_per2 = df_que_per.loc[df_que_per['queueUsagePercentage'] >= queue_per]
df_per_que_message = df_new.loc[df_new['queueUsagePercentage'] >= queue_per]

tb = Texttable()
tb.set_cols_align(['l','r','r'])
tb.set_cols_dtype(['t','i','f'])
tb.header(df_per_que_message.columns.get_values())
tb.add_rows(df_per_que_message.values,header=False)
tb_draw = tb.draw()
html_text = df_per_que_message.to_html(index=False,justify='center',border=5)

title = "The percent of Queue is over %s ,please check !" % queue_per
html_text3 = html_text.replace('class="dataframe">',
                                'class="dataframe"><caption>{}</caption>'.format(title)
                                )
html_text4 = html_text3.replace('<td>', '<td style="height:40px;" align="center" valian="middle">')
que_per2_list = df_que_per2['queueUsagePercentage'].values.T.tolist()
for que in que_per2_list:
    if que > queue_per:
        arrReceiver = ['ops@iyou.com']
        send_mail("New Job valaue is too large in %s" % ResourceManagerUrl, html_text4, arrReceiver)
        print tb_draw
        break
