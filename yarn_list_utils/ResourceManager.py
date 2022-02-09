#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/4/21


from Utils import *




class ResourceManager:

    def __init__(self, rmUrl):
        self.ResourceManager = rmUrl
        self.AppStateUrl = self.ResourceManager + "/ws/v1/cluster/apps"
        self.JobCounterUrl = self.ResourceManager + "/proxy/%s/ws/v1/mapreduce/jobs/%s/counters"
        self.JobInfoUrl = self.ResourceManager + "/proxy/%s/ws/v1/mapreduce/jobs/%s"

        self.ClusterMetrics = self.ResourceManager + "/ws/v1/cluster/metrics"
        self.ScheduceInfoUrl = self.ResourceManager + "/ws/v1/cluster/scheduler"


    def getApplications(self, state="running"):
        url = "%s?state=%s&user.name=%s" % (self.AppStateUrl, state, "yarn")
        return Utils.fetchJsonItems(url, "apps", "app")


    def getAppCounters(self, app, job):
        url = self.JobCounterUrl % (app, job)
        return Utils.fetchJsonItems(url, "jobCounters", "counterGroup")


    def getFileSystemCounters(self, app, job):
        url = self.JobCounterUrl % (app, job)
        groups = Utils.fetchJsonToListItems(url, "jobCounters", "counterGroup")

        for group in groups:
            if group["counterGroupName"] == "org.apache.hadoop.mapreduce.FileSystemCounter":
                return group["counter"]

        return {}


    def getJobInfo(self, app, job):
        url = self.JobInfoUrl % (app, job)
        return Utils.fetchJsonKvItems(url, "job")


    def formatCounterData(self, counterGroups):
        dictField={}

        for counterGroup in counterGroups:
            counters = counterGroup["counter"]

            for counter in counters:
                dictField[counter["name"]] = counter["totalCounterValue"]
                dictField[counter["name"] + "_MAP"] = counter["mapCounterValue"]
                dictField[counter["name"] + "_REDUCE"] = counter["reduceCounterValue"]

        return dictField


    def getScheduceInfo(self):
        return Utils.fetchJsonItems(self.ScheduceInfoUrl, "scheduler", "schedulerInfo")