#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/4/21

import smtplib
import logging
import os

from email.mime.text import MIMEText

#logging.basicConfig(filename = os.path.join(os.getcwd(), 'monitor-hdfs.log'), level = logging.INFO,format = '%(asctime)s - %(levelname)s: %(message)s')


mailto=""
mail_host="smtp.qiye.163.com"
mail_user="data_warning@iyou.com"
mail_pass="Data1qa2ws"
mail_postfix="iyou.com"


def send_mail(sub,content,to):

    me="data_warning"+"<"+mail_user+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ", ".join(to)

    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to, msg.as_string())
        server.close()
        logging.info("MAIL SENT")
        return True

    except Exception as e:
        logging.info("FAIL")
        logging.info(str(e))
        return False

