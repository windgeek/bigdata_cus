#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/5/10

import subprocess
import random
import json

# ./bin/kafka-topics.sh --describe --zookeeper 192.168.148.13:2181/alphadesk --topic __consumer_offsets
def gen_json(file):
    t = []
    # luse = []
    with open(file, 'r') as f:
        for line in f:
            l = []
            a = line.split()
            b = int(a[3].strip())
            c = int(a[5].strip())
            nodes = [1, 2, 3]
            nodes.remove(c)
            r = random.sample(nodes, 2)
            l.append(c)
            l.extend(r)
            # luse.append(c)
            t_json = {
                "topic": "__consumer_offsets",
                "partition": b,
                "replicas": l
            }
            t.append(t_json)
            d = {"version": 1, "partitions": t}
        # print(luse)
        print(json.dumps(d))

if __name__ == '__main__':
    file = './gen.txt'
    gen_json(file)
