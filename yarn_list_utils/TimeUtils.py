#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/4/21


import time


class TimeUtils:


    @staticmethod
    def timeToDatetime(timestamp):
        t = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', t)


    @staticmethod
    def currentTimeToDatetime():
        t = time.localtime(time.time())
        return time.strftime('%Y-%m-%d %H:%M:%S', t)