#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/1/20

from kafka import SimpleClient, KafkaConsumer
from kafka.common import OffsetRequestPayload, TopicPartition

def get_topic_offset(brokers, topic):
    """
    获取一个topic的offset值的和
    """
    client = SimpleClient(brokers)
    partitions = client.topic_partitions[topic]
    offset_requests = [OffsetRequestPayload(topic, p, -1, 1) for p in partitions.keys()]
    offsets_responses = client.send_offset_request(offset_requests)
    return sum([r.offsets[0] for r in offsets_responses])


def get_group_offset(brokers, group_id, topic):
    """
    获取一个topic特定group已经消费的offset值的和
    """
    consumer = KafkaConsumer(bootstrap_servers=brokers,
                             group_id=group_id,
                             )
    pts = [TopicPartition(topic=topic, partition=i) for i in
           consumer.partitions_for_topic(topic)]
    result = consumer._coordinator.fetch_committed_offsets(pts)
    return sum([r.offset for r in result.values()])


if __name__ == '__main__':
    topic_offset = get_topic_offset("172.28.9.1:9092", "dtss-platform-clk")
    group_offset = get_group_offset("172.28.9.1:9092", "ssc-group-2", "dtss-platform-clk")
    lag = topic_offset - group_offset
    print(topic_offset, group_offset, lag)