#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2020/7/22

from kafka import KafkaConsumer

from kafka import KafkaConsumer, TopicPartition

# con = KafkaConsumer(bootstrap_servers = '172.28.9.1:9092')
# tp = TopicPartition('dtss-stats-cvt', 0)
# con.assign([tp])
# con.seek_to_beginning()
# con.seek(tp, 5)
# consumer = KafkaConsumer('dtss-stats-cvt',
#                          bootstrap_servers=['192.168.145.161:9092'])
#
# print consumer.partitions_for_topic("test")  #获取test主题的分区信息
# print consumer.topics()  #获取主题列表
# print consumer.subscription()  #获取当前消费者订阅的主题
# print consumer.assignment()  #获取当前消费者topic、分区信息
# consumer.seek(TopicPartition(topic=u'dtss-stats-cvt', partition=0), 5)  #重置偏移量，从第5个偏移量消费
# print consumer.beginning_offsets(consumer.assignment()) #获取当前消费者可消费的偏移量
# for message in consumer:
# print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
#                                           message.offset, message.key,
#                                           message.value))