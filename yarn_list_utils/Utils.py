#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/4/21

import requests
import json
import time


class Utils:
    '''
    @staticmethod
    def fetchJsonToList(url, root, subitem):

    response = requests.get(url)

    try:
            json_items = json.loads(response.text)
            return json_items[root][subitem]

    except Exception,ex:
            items = []

    return items
    '''

    @staticmethod
    def fetchJsonToListItems(url, root, subitem):
        response = requests.get(url)
        try:
            json_items = json.loads(response.text)
            return json_items[root][subitem]
        except Exception as ex:
            items = []
        return items

    @staticmethod
    def fetchJsonItems(url, root, subitem):
        response = requests.get(url)
        try:
            json_items = json.loads(response.text)
            items = json_items[root][subitem]
        except Exception as ex:
            items = []
        return items

    @staticmethod
    def fetchJsonKvItems(url, root):
        response = requests.get(url)
        try:
            json_items = json.loads(response.text)
            items = json_items[root]
        except Exception as ex:
            items = {}
        return items

    @staticmethod
    def fetchJsonToList(url):
        response = requests.get(url)
        try:
            json_items = json.loads(response.text)
            items = json_items
        except Exception as ex:
            items = []
        return items

    @staticmethod
    def fetchRMJsonKvItems(url, root, key, value):
        result = {}
        response = requests.get(url)
        text = json.loads(response.text)
        items = text[root]
        for item in items:
            if (item.has_key("modelerType")):
                if (item["modelerType"].find("user") != -1): continue
            if item.has_key(key) and item.has_key(value):
                result[item[key]] = item[value]
        return result

    @staticmethod
    def fetchJsonKvsItems(url, root, key, value):
        result = {}
        response = requests.get(url)
        text = json.loads(response.text)
        items = text[root]
        for item in items:
            if (item.has_key("modelerType")):
                if (item["modelerType"].find("user") != -1): continue
            if item.has_key(key):
                result[item[key]] = [item[i] for i in value.split(",")]
        return result

    @staticmethod
    def timeToDatetime(timestamp):
        t = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', t)

    @staticmethod
    def currentTimeToDatetime():
        t = time.localtime(time.time())
        return time.strftime('%Y-%m-%d %H:%M:%S', t)

    @staticmethod
    def getOrDefault(map, key, default):
        if map.has_key(key): return map[key]
        return default

    @staticmethod
    def getOrDefaultByList(list, key, value, default):
        for item in list:
            if item[key] == value: return item
        return default
