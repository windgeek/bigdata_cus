#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2020/7/22

import sys
reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'

from kafka import KafkaConsumer

consumer = KafkaConsumer('mdi-cvt',
                         auto_offset_reset='earliest',
                         bootstrap_servers=['39.107.138.77:9092'])

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
