#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/4/21

from TimeUtils import *
from ResourceManager import *
from optparse import OptionParser
import Mail
import subprocess
import os


ResourceManagerMap = {}
ResourceManagerMap['rm1'] = "resourcemanager14813"
ResourceManagerMap['rm2'] = "resourcemanager14814"


ResourceManagerUrl = "resourcemanager14813"

try:
    for name, url in ResourceManagerMap.items():
        result= subprocess.getstatusoutput('yarn rmadmin -getServiceState %s' % name)
        if result[1] == "active": ResourceManagerUrl = url
except Exception:
    pass



APPLICATION_MASTER = "http://%s:8088" % ResourceManagerUrl
MAIL_BODY = "{} {}\n\n{}\n\n{} \n\n[This job was killed, because it is not registered]"
KILL_LOG_MESSAGE = "{} Kill Application ID : {}; User : {}; Runtime : {}; Name {}\n"


def parseArgs():
    parser = OptionParser(usage="usage: [timeout]")
    parser.add_option('-f', '--file', action='store', dest='file', help='file to handle')
    parser.add_option('-t', '--filet', action='store', dest='filet', help='file to handle')
    (options, args) = parser.parse_args()
    return options



if __name__ == "__main__":
    args = parseArgs()
    config_file = args.file
    config_filet = args.filet
    online_app = []
    with open(config_file, 'r') as f:
        for l in f:
            online_app.append(l.strip())
    with open(config_filet, 'r') as f1:
        for l in f1:
            online_app.append(l.strip())
    print(online_app)
    dt = TimeUtils.currentTimeToDatetime()
    client = ResourceManager(APPLICATION_MASTER)
    apps = client.getApplications()
    apps = sorted(apps,key=lambda app:app["elapsedTime"], reverse=True)
    for app in apps:
        elapsedTime = app["elapsedTime"]
        emails=[]
        appUrl = "%s/cluster/app/%s" % (APPLICATION_MASTER, app["id"])

        emails.append(MAIL_BODY.format(app["id"], app["user"], appUrl, app["name"], elapsedTime / 1000 / 60 / 60))
        if app["user"] == "data-alphadesk": continue
        elif app["user"] == "hive" and app["name"] == "org.apache.spark.sql.hive.thriftserver.HiveThriftServer2": continue
        elif app["name"] == "pdt_jdcloud-data_0601": continue
        elif app["name"] == "TrackingOverallInsight": continue
        elif app["name"] == "OptimusToWarehouseSpark": continue
        elif app["name"].startswith("CrontabTask_TaskId"): continue
        elif app["name"].startswith("AIPL_darlie_"): continue
        elif app["name"] in online_app: continue
        job_owner = app["user"] + "@iyou.com"
        arrReceiver = [job_owner, 'song.li@iyou.com']
        Mail.send_mail("Mip Cluster job killed","\n".join(emails), arrReceiver)
        try:
            print (KILL_LOG_MESSAGE.format(dt, app["id"], app["user"], elapsedTime / 1000 / 60, app["name"]))
        except:
            print (KILL_LOG_MESSAGE.format(dt, app["id"], app["user"], elapsedTime / 1000 / 60, ""))
        print(app['id'])
        # killCommand = "yarn application -kill {}".format(app["id"])
        killCommand = "echo {}".format(app['id'])
        os.popen(killCommand)
